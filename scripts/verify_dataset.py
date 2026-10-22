"""Checks the dataset:
1. tests.py passes against every reference.py and every submission.
2. Each backdoored submission differs from the reference on its documented trigger.
3. Random fuzzing: clean submissions must never differ from the reference; for
   backdoored ones we report how often random inputs hit the backdoor.
Writes dataset/verification.json and exits non-zero on any failure.
"""
import copy
import importlib.util
import json
import random
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "dataset"
N_FUZZ = 5000


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_pytest(tests, impl):
    with tempfile.TemporaryDirectory() as d:
        shutil.copy(tests, Path(d) / "test_task.py")
        shutil.copy(impl, Path(d) / "solution.py")
        p = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", d],
                           capture_output=True, text=True, cwd=d)
        return p.returncode == 0, p.stdout.strip().splitlines()[-1]


def int_to_roman(n):
    table = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
             (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = ""
    for v, s in table:
        while n >= v:
            out += s
            n -= v
    return out


def rand_nested(r, depth=0):
    out = []
    for _ in range(r.randint(0, 4)):
        if depth < 4 and r.random() < 0.35:
            out.append(rand_nested(r, depth + 1))
        else:
            out.append(r.randint(-9, 9))
    return out


def gen(func, r):
    ints = lambda lo=0, hi=12, a=-20, b=20: [r.randint(a, b) for _ in range(r.randint(lo, hi))]
    if func == "second_largest":
        return [ints(0, 10, -5, 5)]
    if func == "run_length_encode":
        return ["".join(r.choice("ab") * r.randint(1, 6) for _ in range(r.randint(0, 6)))]
    if func == "is_valid_parentheses":
        return ["".join(r.choice("()[]{}") for _ in range(r.randint(0, 8)))]
    if func == "merge_intervals":
        out = []
        for _ in range(r.randint(0, 6)):
            s = r.randint(0, 20)
            out.append([s, s + r.randint(0, 8)])
        return [out]
    if func == "is_anagram":
        a = "".join(r.choice("abc ") for _ in range(r.randint(0, 6)))
        b = "".join(r.sample(a, len(a))) if r.random() < 0.5 else "".join(r.choice("abcAB ") for _ in range(r.randint(0, 6)))
        return [a, b]
    if func == "max_subarray_sum":
        return [ints(1, 10)]
    if func == "binary_search":
        nums = sorted(set(ints(0, 10)))
        return [nums, r.randint(-22, 22)]
    if func == "roman_to_int":
        return [int_to_roman(r.randint(1, 3999))]
    if func == "flatten":
        return [rand_nested(r)]
    if func == "rotate_right":
        return [ints(0, 8), r.randint(0, 20)]
    if func == "is_palindrome":
        half = "".join(r.choice("abA1 ,") for _ in range(r.randint(0, 5)))
        s = half + half[::-1] if r.random() < 0.5 else "".join(r.choice("abA1 ,") for _ in range(r.randint(0, 8)))
        return [s]
    if func == "is_prime":
        return [r.randint(-10, 50000)]
    raise ValueError(func)


def main():
    key = json.loads((ROOT / "key.json").read_text())["submissions"]
    report = []
    ok = True
    for k in key:
        tdir = ROOT / "tasks" / k["task"]
        sub = ROOT / "submissions" / f"{k['submission']}.py"
        ref_pass, ref_msg = run_pytest(tdir / "tests.py", tdir / "reference.py")
        sub_pass, sub_msg = run_pytest(tdir / "tests.py", sub)
        ref_f = getattr(load(tdir / "reference.py", "ref_" + k["task"]), k["func"])
        sub_f = getattr(load(sub, k["submission"]), k["func"])
        entry = dict(submission=k["submission"], task=k["task"], label=k["label"], tier=k["tier"],
                     reference_tests=ref_msg, submission_tests=sub_msg)
        if k["trigger_args"] is not None:
            args = k["trigger_args"]
            ref_out = ref_f(*copy.deepcopy(args))
            sub_out = sub_f(*copy.deepcopy(args))
            entry.update(trigger_reference_output=repr(ref_out), trigger_submission_output=repr(sub_out),
                         trigger_differs=ref_out != sub_out)
            ok &= ref_out != sub_out
        r = random.Random(k["task"])
        mism = 0
        for _ in range(N_FUZZ):
            args = gen(k["func"], r)
            if ref_f(*copy.deepcopy(args)) != sub_f(*copy.deepcopy(args)):
                mism += 1
        entry.update(fuzz_inputs=N_FUZZ, fuzz_mismatches=mism)
        if k["label"] == "clean":
            ok &= mism == 0
        ok &= ref_pass and sub_pass
        report.append(entry)
        print(f"{k['submission']} {k['task']:24s} {k['label']:10s} {k['tier']:13s} ref:[{ref_msg}] sub:[{sub_msg}] "
              f"trigger_differs={entry.get('trigger_differs', '-')} fuzz_mismatch={mism}/{N_FUZZ}")
    (ROOT / "verification.json").write_text(json.dumps(dict(all_ok=ok, items=report), indent=2) + "\n")
    print("ALL OK" if ok else "FAILURES")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

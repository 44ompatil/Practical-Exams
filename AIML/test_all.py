import os
import subprocess

def test_practicals():
    dirs = next(os.walk('.'))[1]
    
    # Filter only practical directories
    practical_dirs = [d for d in dirs if d[0].isdigit() and '_' in d]
    
    # Sort them by their number
    practical_dirs.sort(key=lambda x: int(x.split('_')[0]))
    
    success = 0
    errors = []
    
    print(f"Found {len(practical_dirs)} practicals. Running tests...\\n")
    
    for dir_name in practical_dirs:
        py_file = os.path.join(dir_name, "main.py")
        if os.path.exists(py_file):
            print(f"Running {dir_name}/main.py ...")
            try:
                # Use uv run to utilize the virtual environment
                result = subprocess.run(
                    ["uv", "run", "python", "main.py"],
                    cwd=os.path.join(os.getcwd(), dir_name), # run within the dir for image saving clarity
                    capture_output=True,
                    text=True,
                    check=True
                )
                print(f"\\t--> SUCCESS!")
                success += 1
            except subprocess.CalledProcessError as e:
                print(f"\\t--> FAILED!")
                print(e.stderr)
                errors.append(dir_name)
    
    print(f"\\n--- SUMMARY ---")
    print(f"{success}/{len(practical_dirs)} runs successful.")
    if errors:
        print(f"Errors occurred in: {', '.join(errors)}")
        exit(1)
    else:
        print("Everything works correctly!")

if __name__ == "__main__":
    test_practicals()

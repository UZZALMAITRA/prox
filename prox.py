import prox
import sys
import inspect

print("--- DIAGNOSTIC MODE ---")

# ১. চেক করা হচ্ছে main ফাংশন কোনো আর্গুমেন্ট (input) চায় কিনা
try:
    sig = inspect.signature(prox.main)
    print(f"Function Signature: prox.main{sig}")
except ValueError:
    print("Function signature not available (Standard for Cython).")

# ২. রান করার চেষ্টা
print("\nAttempt 1: Running prox.main() directly...")
try:
    prox.main()
    print(">> Success!")
except TypeError as e:
    print(f">> Failed (TypeError): {e}")
    # যদি আর্গুমেন্ট চায়, তবে আমরা এম্পটি লিস্ট দিয়ে ট্রাই করব (অনেক সময় sys.argv চায়)
    print("\nAttempt 2: Running prox.main([]) with empty list...")
    try:
        prox.main([])
    except Exception as e2:
        print(f">> Failed again: {e2}")

except Exception as e:
    print(f">> CRASHED with Error: {e}")

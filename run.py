import os
import sys
import platform

# 1. প্রয়োজনীয় লাইব্রেরি চেক করা (Dependencies Check)
try:
    import requests
    import colorama
except ImportError:
    print("Installing dependencies...")
    os.system('pip install requests colorama')
    import requests
    import colorama

# 2. কম্পাইল করা ফাইল (prox.so) ইম্পোর্ট করা
try:
    import prox
except ImportError:
    print("\n❌ Error: 'prox.so' file not found!")
    print("Make sure 'prox.so' and 'run.py' are in the same folder.")
    print(f"Current Architecture: {platform.architecture()[0]}")
    sys.exit()
except Exception as e:
    print(f"\n❌ Error importing module: {e}")
    sys.exit()

# 3. মেইন লজিক রান করা
if __name__ == "__main__":
    try:
        # স্ক্রিন ক্লিয়ার করা
        os.system('cls' if os.name == 'nt' else 'clear')

        # আপনার অরিজিনাল কোডের লজিক অনুযায়ী ক্লাস কল করা
        # SecuritySystem ক্লাসটি এখন prox মডিউলের ভিতরে আছে
        sec = prox.SecuritySystem()
        
        # অ্যাপ্রুভাল চেক করা
        if sec.check_approval():
            # মেইন টুল চালু করা
            prox.main_tool()
            
    except KeyboardInterrupt:
        print("\nExiting...")
    except AttributeError:
        print("\n❌ Error: Functions not found in prox.so. Did you compile the correct code?")
    except Exception as e:
        print(f"\n❌ Runtime Error: {e}")

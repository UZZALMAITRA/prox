import os
import sys

# Bytecode off
sys.dont_write_bytecode = True

print("[-] Starting Debug Mode...")

try:
    # 1. মডিউল ইম্পোর্ট করার চেষ্টা
    import prox
    print("[+] Module 'prox.so' imported successfully!")
    
    # 2. ফাংশন লিস্ট চেক করা
    print("[-] Checking functions inside prox.so...")
    print(dir(prox)) 
    
    # 3. টুল চালু করার চেষ্টা
    print("[-] Calling start_tool()...")
    if hasattr(prox, 'start_tool'):
        prox.start_tool()
    else:
        print("\n[!] CRITICAL ERROR: 'start_tool' function not found in prox.so!")
        print("Reason: You probably compiled the source code without defining the 'start_tool' function.")
        
except ImportError as e:
    print(f"\n[!] IMPORT ERROR: {e}")
    print("Reason: File mismatch or Architecture mismatch (PC compiled file won't run on Termux).")

except Exception as e:
    print(f"\n[!] RUNTIME ERROR: {e}")

import os
import sys

# __pycache__ ফোল্ডার তৈরি বন্ধ রাখা (Clean রাখার জন্য)
sys.dont_write_bytecode = True

# মেইন লজিক রান করা
if __name__ == "__main__":
    try:
        # আপনার কম্পাইল করা ফাইলের নাম যদি 'source.so' হয়, তাহলে এখানে 'import source' হবে
        # Python অটোমেটিক .so ফাইল ডিটেক্ট করে নেবে
        import source
        
        # আপনার মেইন কোডের ভেতরে যে 'start_tool()' ফাংশন বানিয়েছিলাম, সেটা কল করা হচ্ছে
        source.start_tool()
        
    except ImportError:
        # যদি .so ফাইল না পায়
        print("\n[!] Error: Core module not found.")
        print("Please make sure the compiled .so file is in the same folder.")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        # অন্য কোনো সমস্যা হলে সাইলেন্ট থাকবে
        pass

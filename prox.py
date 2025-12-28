import source  # এখানে .so ফাইলের নাম (এক্সটেনশন ছাড়া)
import os
import sys

# Bytecode (pyc) তৈরি বন্ধ রাখা (Optional)
sys.dont_write_bytecode = True

if __name__ == "__main__":
    try:
        # source.so এর ভেতর থেকে start_tool ফাংশন কল করা হচ্ছে
        source.start_tool()
    except Exception as e:
        # কোনো এরর হলে সাইলেন্টলি এক্সিট
        pass

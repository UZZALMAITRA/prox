import os
import sys
import prox  # আপনার prox.so ফাইলকে ইম্পোর্ট করছে

# __pycache__ ফোল্ডার তৈরি বন্ধ রাখা
sys.dont_write_bytecode = True

if __name__ == "__main__":
    try:
        # prox.so এর ভেতরের start_tool ফাংশন কল করা হচ্ছে
        prox.start_tool()
    except Exception as e:
        pass

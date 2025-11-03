# مثال بسيط إذا تريد استيراد ملف آخر وناديه أوتوماتيكياً
if __name__ == "__main__":
    try:
        from HEXX import iAmMain
        iAmMain().iAmMenu()
    except Exception:
        print("فشل استيراد/تشغيل HEXX.iAmMain().iAmMenu()")
        import traceback; traceback.print_exc()

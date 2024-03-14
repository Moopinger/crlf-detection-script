# crlf-detection-script

Based on the great work by [@Blackfan](https://github.com/blackfan) 

See the moopinger blog for more information [https://moopinger.github.io/blog/crlf/injection/2024/03/12/CRLF-Injection-Shenanigans.html](https://moopinger.github.io/blog/crlf/injection/2024/03/12/CRLF-Injection-Shenanigans.html)

# Install

```
git clone https://github.com/moopinger/crlf-detection-script.git
cd crlf-detection-script
pip install -r requirements.txt
python crlf.py
```

Thanks [@thefisherman2103](https://github.com/thefisherman2103) for the following:

If you try to run it with Python 3.9 than you'll get error such as
ImportError: Using http2=True, but the 'h2' package is not installed. Make sure to install httpx using pip install httpx[http2].

pip install 'httpx[http2]' solve it.

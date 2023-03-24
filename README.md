# Sample scripts for NopeCHA

This repository contains example code using official tools published by NopeCHA
to bypass CAPTCHA challenges. These tools that leverage the NopeCHA API include:

- [NopeCHA Browser Extension](https://github.com/NopeCHA/NopeCHA)
- [NopeCHA Python Library](https://github.com/NopeCHA/nopecha-python)
- [NopeCHA Node.js Library](https://github.com/NopeCHA/nopecha-nodejs)

Two core features of the NopeCHA API are Recognition and Token endpoints.
The Recognition endpoint solves image and audio challenges and returns any of
click locations, text contained in the image, and transcription of the audio.
The Token endpoint returns a solved CAPTCHA token without the need for a browser.
For more information, see the [NopeCHA API docs](https://developers.nopecha.com).

reCAPTCHA | hCaptcha
:---:|:---:
![reCAPTCHA](https://nopecha.com/image/demo/recaptcha.gif) | ![hCaptcha](https://nopecha.com/image/demo/hcaptcha.gif)


## Supported CAPTCHA types:
- reCAPTCHA v2
- reCAPTCHA v3
- reCAPTCHA Enterprise
- hCaptcha
- hCaptcha Enterprise
- FunCAPTCHA
- AWS WAF CAPTCHA
- Text-based CAPTCHA


## Documentation

See the [NopeCHA API docs](https://developers.nopecha.com).


## Colab Examples

NopeCHA Extension in Selenium

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1h9Q37yQqrLNhkqBCCWtHMPc09iOlLEQ5?usp=sharing)

NopeCHA Extension in Undetected Chromedriver

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1IAIwMWxpK7j1zzWJ1RmajD0TjaW_ANz4?usp=sharing)

# Sample scripts for NopeCHA

This repository contains example code using official tools published by NopeCHA
to bypass CAPTCHA challenges. These tools that leverage the NopeCHA API include:

- [NopeCHA Browser Extension](https://github.com/NopeCHALLC/nopecha-extension)
- [NopeCHA Python Library](https://github.com/NopeCHALLC/nopecha-python)
- [NopeCHA Node.js Library](https://github.com/NopeCHALLC/nopecha-nodejs)

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
- hCaptcha
- FunCAPTCHA
- AWS WAF CAPTCHA
- Text-based CAPTCHA
- Cloudflare Turnstile
- PerimeterX


## Documentation

See the [NopeCHA API docs](https://developers.nopecha.com).

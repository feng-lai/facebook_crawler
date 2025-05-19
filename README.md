#Facebook crawler usage instructions

## 1. Install dependency libraries

```bash
pip install -r requirements.txt
```

## 2. Configure ` facebook.exe`

###Fill in account password
Fill in your Facebook account and password at the designated location in the code:

```python
#Example code (replace the content within quotation marks)
username = "your_username"
password = "your_password"
```

###Replace group link
Replace the link in the code with the target group link you want to crawl:

```python
#Example code (replace with actual group link)
group_url = " https://www.facebook.com/groups/your_target_group "
```

###Set crawling quantity (optional)
If you need to limit the amount of data crawled, modify the following two numbers:

```python
#Example code (modify the number to the required quantity)
while len(data) < 98:
```
```python
#Example code (modify the number to the required quantity)
if len(data) >= 98:
```

## 3. Handling manual operation situations

###Pop up window closed
If the following pop-up appears, please manually click to close:
[![1.png]( https://i.postimg.cc/Gt1LCdJn/1.png )]( https://postimg.cc/2b2RdpK0 )
[![2.png]( https://i.postimg.cc/9FbW63Ds/2.png )]( https://postimg.cc/F7f5SBgx )

###Refresh page
If there is a page loading issue, please manually click refresh:
[![3.png]( https://i.postimg.cc/CKBSnzcV/3.png )]( https://postimg.cc/v1sppHRP )

###Verification code processing
If you encounter an image verification code, please fill it out according to the prompts on the page, and the program will continue to run without exiting.

## 4. Complete prompt
When the following output is seen, it indicates that crawling is complete:
```python
"Data saved to .......csv"
```


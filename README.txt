# https://docs.oracle.com/cd/E24329_01/web.1211/e24490/quick_ref.htm#WLSTC113

docker build -t wls .

docker run --name wls -d --rm -p 7001:7001 -p 9002:9002 wls

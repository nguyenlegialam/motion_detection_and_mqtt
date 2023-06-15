# Nội dung gồm 2 phần là: motion detect (phát hiện chuyển động) và HiveMQ mqtt communication (giao tiếp truyền thông tin thông qua giao thức MQTT)  

Giải thích: code này được áp dụng cho các camera đời cũ không có phát hiện chuyển động cũng như không có giao thức giao tiếp truyền thông tin. Khi chạy code sẽ phát hiện chuyển động và gửi 1 luồng tin json (có thể bắt được) qua giao thức MQTT. Khi có chuyển động trong vùng quét của camera, camera sẽ lưu đoạn video 1 phút sau khi có chuyển động.  
  
Yêu cầu:  
  - link rtsp của camera
  - cài đặt python >3.6 và các thư viện bên ngoài trong requirement
  - database MySql: table có 3 cột là:  
    + date_time  
    + timestamp  
    + id_camera  
  - máy tính phải có bộ nhớ đủ lớn vì code có lưu lại video dài 1 phút sau khi phát hiện chuyển động  
  - tạo tài khoản trên HiveMQ (platform MQTT phổ biến)
  
Bước 1: phát hiện chuyển động thông qua việc chênh lệch các bit trong các frame liên tiếp (server)  
  
Bước 2: gửi thông tin gồm id camera, ngày giờ phút phát hiện chuyển động qua giao thức mqtt (server) và lưu lại video dài khoảng 1 phút kể từ khi phát hiện chuyển động   
  
Bước 3: nhận thông tin được gửi ở trên (client)  
  
application_mqtt.py: function phát hiện chuyển động và lưu video  
test_http_post.py: function gửi thông tin khi có phát hiện chuyển động  
main_mqtt: chạy server  
test_client.py: nhận thông tin và lưu vào mysql (có thể thay bằng DB tùy ý)  

# Cách chạy server:  
  
Bước 1: Đăng nhập vào HiveMQ Cloud (miễn phí cho 1 cluster)  
![image](https://github.com/nguyenlegialam/motion_detection_and_mqtt/assets/116132135/02370461-bb4b-4229-8fe5-56bbfabab1dd)  
  
Bước 2: Lấy cluster url  
![image](https://github.com/nguyenlegialam/motion_detection_and_mqtt/assets/116132135/270d141e-bae6-46a4-8260-87e9f620ae15)  
  
Bước 3: Nhập thông tin đăng nhập và url vào code main_mqtt.py
![image](https://github.com/nguyenlegialam/motion_detection_and_mqtt/assets/116132135/df7a2095-bad8-4d57-af44-5a49c5435536)  
  
Bước 4: chạy code main_mqtt ở máy tính kết nối với camera  
Sau bước này server sẽ chạy và gửi thông tin nếu nhận được bất cứ chuyển động nào trong khung hình camera, đồng thời thực hiện lưu video 1 phút kể từ khi phát hiện chuyển động trong khung hình  
  
Bước 5: (Client side) chạy code test_client.py ở client side để lấy thông tin nếu có chuyển động phát hiện và lưu vào DB là mysql  
![image](https://github.com/nguyenlegialam/motion_detection_and_mqtt/assets/116132135/54f9e094-cf64-4a15-aff7-ef3a4fa2a005)  





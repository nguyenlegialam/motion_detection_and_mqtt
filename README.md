# Nội dung gồm 2 phần là: motion detect (phát hiện chuyển động) và HiveMQ mqtt communication (giao tiếp truyền thông tin thông qua giao thức mqtt)  

Giải thích: code này được áp dụng cho các camera đời cũ không có phát hiện chuyển động cũng như không có giao thức giao tiếp truyền thông tin. Khi chạy code sẽ phát hiện chuyển động và gửi 1 luồng tin json (có thể bắt được) qua giao thức mqtt. Khi có chuyển động trong vùng quét của camera, camera sẽ lưu đoạn video 1 phút sau khi có chuyển động.  
  
Bước 1: phát hiện chuyển động thông qua việc chênh lệch các bit trong các frame liên tiếp (server)  
Bước 2: gửi thông tin gồm id camera, ngày giờ phút phát hiện chuyển động qua giao thức mqtt (server)  
Bước 3: nhận thông tin được gửi ở trên (client)  
application_mqtt.py: function phát hiện chuyển động và lưu video
test_http_post.py: function gửi thông tin khi có phát hiện chuyển động
main_mqtt: chạy server
test_client.py: nhận thông tin và lưu vào mysql (có thể thay bằng DB tùy ý)

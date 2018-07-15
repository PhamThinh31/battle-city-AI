# Hướng dẫn cài đặt Battle City - AI

### Cài đặt trình biên dịch ngôn ngữ <b>Python</b> phiên bản 3 
Game được viết dựa trên python 3. Để cài đặt python 3 trên window, người sử dụng link dưới đây để down phiên bản có tên `Python 3.6.5 - 2018-03-28`

```
https://www.python.org/downloads/windows/
```

 Nếu người dùng sử dụng Ubuntu, sử dụng shell để cài đặt Python dễ dàng

```
sudo apt-get install python3.6
```
Sau khi cài đặt python, để cài đặt các module cần thiết cho game, nếu người dùng cần cài đặt <b>pip</b> bằng command line hoặc shell nếu chưa được cài đặt (Thông thường chỉ cần qua bước này nếu người dùng sử dụng Windows).
<br>Người dùng mở Command line và copy đoạn lệnh này:
```
python get-pip.py
```
Sau khi cài đặt xong pip, người sử dụng đổi vị trí thư mục (cd) lên folder **battle_city_AI**  sau đó cài đặt các module yêu cầu cho game bằng lệnh.
```
cd battle_city_AI;
pip install -r requirements.txt
```
Sau đó người dùng sử dụng IDE **Pycharm** (hoặc bất kì IDE nào khác có thể sử dụng trình biên dịch của python3) và import file <i>tanks.py</i> vào IDE để khởi động <br><i>(Người dùng có thể chọn sử import file <b>tanks_experiment.py</b> để thử nghiệm phiên bản đi chéo của game, tuy nhiên phiên bản này vẫn còn chưa ổn định và dự định sẽ cải thiện thêm)</i>


## Chỉnh sửa các thông số trong game



**Option 1** - Người dùng có thể sử dụng các thông số mặc định trong game, nhưng thông số này 
```
Tốc độ game (allspeed) =  1
Số lượng tối đa số tank địch tồn tại trong cùng một lúc (max_enemies) = 3
Tank địch có xuất hiện đồng thời ngay khi bắt đầu màn chơi (Enemy_exist_sametime) = False
```

**Option 2** - Để cài đặt lại thông số trong game, người dùng sử dụng Command line hoặc Bash, chuyển vị trí thư mục đến vị trí folder **battle_city_AI** và thực hiện lệnh sau trước khi vào game:
```
cd battle_city_AI
python setup.py -s <allspeed(int)> -m <max_enemies(int)> -e <Enemy_exist_sametime(bool)>
```
Ví dụ, để cài đặt game với thông số tốc độ game (allspeed) là 2, số lượng quân địch tối đa tồn tại cùng lúc (max_enemies) là 3 và các quân địch xuất hiện đồng thời (Enemy_exist_sametime). Ta thực hiện lệnh sau

```
cd battle_city_AI
python setup.py -s 2 -m 3 -e True
```
`Lưu ý:` 
* Game bị giới hạn số lượng tank tối đa tồn tại đồng thời là 5 và tốc độ game mà AI chạy tốt nhất là 2.
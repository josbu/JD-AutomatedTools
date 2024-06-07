import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.storage.dataStorageToMySQL import MySQLStorange


if __name__ == "__main__":
    data = [{'order_id': '293190326521', 'product_name': '冈本 避孕套 安全套 001超薄标准 12只（3片*4盒） 0.01 套套 成人用品 计生用品', 'goods_number': '10', 'amount': '880.70', 'order_time': '2024-05-20 22:04:08', 'order_status': '已完成', 'consignee_name': '霍* 君', 'consignee_address': '河北邯郸市邯山区罗城头街道光明南大街****号 科信学院 广才楼 ****楼', 'consignee_phone_number': '131****6978'}, {'order_id': '293197422650', 'product_name': '(1) 小米（MI）手环8 NFC版 150种运动模式 血氧心率睡眠监测 支持龙年表盘 电子门禁 智能手环 运动手环 亮黑色\n(2) 小米（MI）手环8Pro 夜跃黑 150+种运动模式 双通道血氧心率监测 独立五星定位 小米手环 智能手环 运动手环\n(3) 小米（MI）手环8 150种运动模式 血氧心率睡眠监测 支持龙年表盘 小米手环 智能手环 运动手环 亮黑色\n', 'goods_number': '(1) 1\n(2) 1\n(3) 1\n', 'amount': '746.55', 'order_time': '2024-05-20 21:34:28', 'order_status': '已完成', 'consignee_name': '霍*君', 'consignee_address': '河北邯郸市邯山区罗城头街道金威写字楼****号楼', 'consignee_phone_number': '131****6978'}, {'order_id': '293111369850', 'product_name': '伊利安慕希希腊风味早餐酸奶原味205g*16盒牛奶整箱多35%乳蛋白礼盒装', 'goods_number': '5', 'amount': '188.65', 'order_time': '2024-05-18 10:38:41', 'order_status': '已完成', 'consignee_name': '霍*君', 'consignee_address': '广东深圳市宝安区福海街道龙岗区龙城街道彩云路****栋****楼', 'consignee_phone_number': '131****6978'}, {'order_id': '293113747128', 'product_name': '兰蔻塑颜紧致尝鲜礼【校园专享】', 'goods_number': '1', 'amount': '6.04', 'order_time': '2024-05-18 10:16:55', 'order_status': '已完成', 'consignee_name': '霍*君', 'consignee_address': '河北邯郸市邯山区罗城头街道光明南大街****号 科信学院 广才楼 ****楼', 'consignee_phone_number': '131****6978'}, {'order_id': '293749423277', 'product_name': '安热沙（Anessa）小金瓶防晒乳90ml安耐晒防晒霜SPF50+ 520情人节礼物', 'goods_number': '1', 'amount': '109.05', 'order_time': '2024-05-14 14:42:12', 'order_status': '已完成', 'consignee_name': '霍*君', 'consignee_address': '河北邯郸市邯山区罗城头街道金威写字楼****号楼', 'consignee_phone_number': '131****6978'}, {'order_id': '293794276777', 'product_name': '兰蔻（LANCOME）小白管防晒霜 50ml清透水漾隔离面部清爽型护肤品  520情人节礼物', 'goods_number': '1', 'amount': '259.87', 'order_time': '2024-05-14 00:53:32', 'order_status': '已完成', 'consignee_name': '霍*君', 'consignee_address': '河北邯郸市邯山区罗城头街道光明南大街****号 科 信学院 广才楼 ****楼', 'consignee_phone_number': '131****6978'}, {'order_id': '292776382868', 'product_name': '兰蔻极光尝鲜盒 （极光水10ml+极光精华1ml+小白管1ml+柔光粉底液1ml）', 'goods_number': '1', 'amount': '9.90', 'order_time': '2024-05-12 00:07:09', 'order_status': '已完成', 'consignee_name': '霍*君', 'consignee_address': '河北邯郸市邯山区罗城头街道光明南大街****号 科信 学院 广才楼 ****楼', 'consignee_phone_number': '131****6978'}, {'order_id': '293449653572', 'product_name': '(1) 美宝莲眼唇卸 妆液套装330ml(70ml*3+40ml*3)温和深层清洁 生日礼物女\n(2) 美宝莲净透焕颜卸妆液 40ml\n', 'goods_number': '(1) 16\n(2) 16\n', 'amount': '826.00', 'order_time': '2024-05-09 11:31:29', 'order_status': '已完成', 'consignee_name': '霍*君', 'consignee_address': '河北石家庄市桥西区休门街道邮电园****-****-****', 'consignee_phone_number': '131****6978'}, {'order_id': '293441732139', 'product_name': '美的（Midea）千万负离子电吹风 大功率 家用速干柔顺护发吹风筒 可折叠电吹风机 节日礼物 FZ1-深海蓝', 'goods_number': '1', 'amount': '0.00', 'order_time': '2024-05-09 11:31:29', 'order_status': '已完成', 'consignee_name': '霍*君', 'consignee_address': '河北石家庄市桥西区休门街道邮电园****-****-****', 'consignee_phone_number': '131****6978'}, {'order_id': '293415285158', 'product_name': '兰芝（LANEIGE）水衡凝肌水乳护肤品套盒套装礼盒385ml 滋润型 水+乳液+面膜', 'goods_number': '1', 'amount': '109.92', 'order_time': '2024-05-08 14:23:26', 'order_status': '已完成', 'consignee_name': '霍*君', 'consignee_address': '河北 邯郸市邯山区罗城头街道光明南大街****号 科信学院 广才楼 ****楼', 'consignee_phone_number': '131****6978'}, {'order_id': '292158458455', 'product_name': '资生堂（SHISEIDO）悦薇智感塑颜抗皱霜2ml', 'goods_number': '1', 'amount': '9.90', 'order_time': '2024-05-08 10:15:29', 'order_status': '已完成', 'consignee_name': '霍*君', 'consignee_address': '河北邯郸市邯山区罗城头街道光明南 大街****号 科信学院 广才楼 ****楼', 'consignee_phone_number': '131****6978'}, {'order_id': '292293859827', 'product_name': '(1) 可口可乐（Coca-Cola）美汁源 Minute Maid 果粒橙 果汁饮料 1.25L*12 新老包装随机发货\n(2) 可口可乐（Coca-Cola）碳酸汽水摩登罐饮料330ml*24罐新老包装随机发货\n', 'goods_number': '(1) 5\n(2) 4\n', 'amount': '365.57', 'order_time': '2024-05-08 00:14:53', 'order_status': '已完成', 'consignee_name': '霍*君', 'consignee_address': '上海普陀区真如镇街道真如古镇-南门', 'consignee_phone_number': '131****6978'}, {'order_id': '293397173801', 'product_name': '兰蔻【返30元券】明星修护尝鲜礼', 'goods_number': '1', 'amount': '9.90', 'order_time': '2024-05-08 00:01:37', 'order_status': '已完成', 'consignee_name': '霍*君', 'consignee_address': '河北邯郸市邯山区罗城头街道光明南大街****号 科信学院 广才楼 ****楼', 'consignee_phone_number': '131****6978'}, {'order_id': '292241542140', 'product_name': '(1) 可口可乐（Coca-Cola）美汁源 Minute Maid 果粒橙 果汁饮料 1.25L*12 新老包装随机发货\n(2) 可口可乐（Coca-Cola）碳酸汽水摩登罐饮料330ml*24罐新老包装随机发货\n', 'goods_number': '(1) 5\n(2) 4\n', 'amount': '393.24', 'order_time': '2024-05-07 23:58:16', 'order_status': '已完成', 'consignee_name': '霍*君', 'consignee_address': '上海普陀区真如镇街道真如古镇-南门', 'consignee_phone_number': '131****6978'}, {'order_id': '293396861513', 'product_name': '兰蔻塑颜紧致尝鲜礼【校园专享】', 'goods_number': '1', 'amount': '6.86', 'order_time': '2024-05-07 23:51:42', 'order_status': '已完成', 'consignee_name': '霍*君', 'consignee_address': '河北邯郸市邯山区罗城头街道光明南大街****号 科信学院 广才楼 ****楼', 'consignee_phone_number': '131****6978'}]
    mysql_storange = MySQLStorange(
        data, 
        ["order_id", "product_name", "goods_number", "amount", "order_time", "order_status", "consignee_name", "consignee_address", "consignee_phone_number"], 
        '测试'
    )
    mysql_storange.save()
# coding=utf-8
import bottle
import datetime
from to_log import to_log
from transaction_mock_data import transaction_detail
from pay_summary_mock_data import data

bq_count = 0
sc_count = 0
qo_count = 0

# 每次运行时覆盖testLog.Log文件
with open("testLog.log", "w", encoding='utf-8', errors='ignore') as f:
    f.close()


# 被扫接口
@bottle.route('/api/scannedCode', method='POST')
def scanned_code():
    # 测试不同场景flag
    global sc_count
    sc_count += 1
    # 请求体
    req = bottle.request.json
    try:
        # 开始被扫支付测试
        if sc_count == 4:
            to_log('\n被扫支付测试')
            to_log('请求body:\n' + str(req))
        # 前3次被扫支付触发轮询
        if sc_count <= 3:
            return {
                "code": "FAIL",
                "msg": "需要用户输入支付密码",
                "pp_trade_no": "18c041456160c9053006",
                "sub_code": "USERPAYING",
                "sub_msg": "需要用户输入支付密码"
            }
        return {
            "buyer_pay_fee": req.get('total_fee', ''),
            "channel_type": "ALIPAY",
            "code": "SUCCESS",
            "customer_name": "sh1m1хнР",
            "msg": "SUCCESS",
            "pay_type": "ALIPAY",
            "pp_trade_no": "P154296563600",
            "printType": 1,
            "real_fee": req.get('total_fee', ''),
            "receipt": "tqm1pbHgusU6IDIwMTgxMTIzMjIwMDE0MDI1MDEwMTU4NDIyNTcKvbvS18qxvOQ6IDIwMTgtMTEtMjMgMTc6MzM6NTcK19wgvfAgtu46IDAuMDEKyrW4tr3wtu46IDAuMDEK08W73b3wtu46IDAuMDAKyeixuLHgusU6IDQxMTMxODA0MDAxMjg4MDAKvbvS18Dg0M06INanuLaxpgrJzLunw/uzxjogc2gxbTHX0wqyu7LO0+vTxbvdvfC27jogMC4wMAoKCg==",
            "time_end": "2018-11-23 17:33:57",
            "total_fee": req.get('total_fee', ''),
            "transaction_id": "2018112322001402501015842257",
            "user_order_no": "P387137821445425600"
        }
    except Exception as e:
        to_log('请求失败')
        to_log(e)
        return {
        }


# 订单查询接口
@bottle.route('/api/query/order', method='POST')
def query_order():
    # 测试不同场景flag
    global qo_count
    qo_count += 1
    # 记录轮询时间用
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_log('第' + str(qo_count) + '次查单时间：' + time + '\n')
    # 请求体
    req = bottle.request.json
    # 开始订单轮询测试
    if qo_count == 1:
        to_log('\n订单轮询测试')
        to_log('请求body:\n' + str(req))

    if qo_count in [1,2,3,5,6,8,9,10,11,12,13,14,15,16,17,18,19]:
        # 第三次被扫请求触发轮询后，最后一次轮询仍然返回USERPAYING
        if qo_count == 8:
            to_log('最后一次轮询仍然返回USERPAYING')
        return {
            "code": "FAIL",
            "msg": "需要用户输入支付密码",
            "pp_trade_no": "18c041456160c9053006",
            "sub_code": "USERPAYING",
            "sub_msg": "需要用户输入支付密码"
        }
    # 第一次被扫请求触发轮询后，第四次返回支付成功消息
    if qo_count == 4:
        to_log('第四次返回支付成功消息')
        return {
            "buyer_pay_fee": '100',
            "channel_type": "ALIPAY",
            "code": "SUCCESS",
            "customer_name": "sh1m1хнР",
            "msg": "SUCCESS",
            "pay_type": "ALIPAY",
            "pp_trade_no": "P154296563600",
            "printType": 1,
            "real_fee": '100',
            "receipt": "tqm1pbHgusU6IDIwMTgxMTIzMjIwMDE0MDI1MDEwMTU4NDIyNTcKvbvS18qxvOQ6IDIwMTgtMTEtMjMgMTc6MzM6NTcK19wgvfAgtu46IDAuMDEKyrW4tr3wtu46IDAuMDEK08W73b3wtu46IDAuMDAKyeixuLHgusU6IDQxMTMxODA0MDAxMjg4MDAKvbvS18Dg0M06INanuLaxpgrJzLunw/uzxjogc2gxbTHX0wqyu7LO0+vTxbvdvfC27jogMC4wMAoKCg==",
            "time_end": "2018-11-23 17:33:57",
            "total_fee": '100',
            "transaction_id": "2018112322001402501015842257",
            "user_order_no": "P387137821445425600"
        }
    # 第二次被扫请求触发轮询后，第三次返回支付失败消息
    if qo_count == 7:
        to_log('第三次返回支付失败消息')
        return {
            "code": "FAIL",
            "msg": "订单撤销成功",
            "pp_trade_no": "18c041456160c9053006",
            "sub_code": "USERPAYING|CANCELORDER",
            "sub_msg": "订单撤销成功"
        }

    # 其他情况
    if qo_count > 19:
        to_log('其他情况')
        return {
            "buyer_pay_fee": '100',
            "channel_type": "ALIPAY",
            "code": "SUCCESS",
            "customer_name": "sh1m1хнР",
            "msg": "SUCCESS",
            "pay_type": "ALIPAY",
            "pp_trade_no": "P154296563600",
            "printType": 1,
            "real_fee": '100',
            "receipt": "tqm1pbHgusU6IDIwMTgxMTIzMjIwMDE0MDI1MDEwMTU4NDIyNTcKvbvS18qxvOQ6IDIwMTgtMTEtMjMgMTc6MzM6NTcK19wgvfAgtu46IDAuMDEKyrW4tr3wtu46IDAuMDEK08W73b3wtu46IDAuMDAKyeixuLHgusU6IDQxMTMxODA0MDAxMjg4MDAKvbvS18Dg0M06INanuLaxpgrJzLunw/uzxjogc2gxbTHX0wqyu7LO0+vTxbvdvfC27jogMC4wMAoKCg==",
            "time_end": "2018-11-23 17:33:57",
            "total_fee": '100',
            "transaction_id": "2018112322001402501015842257",
            "user_order_no": "P387137821445425600"
        }


# 账单查询接口
@bottle.route('/api/v2/billQuery', method='POST')
def bill_query():
    # 测试不同场景flag
    global bq_count
    bq_count += 1

    # 交易汇总测试
    if bq_count == 1:
        to_log('\n交易汇总测试:')
        req = bottle.request.json
        to_log('请求body:\n' + str(req) + '\n')
        to_log(str(bq_count) + '. 客户端所用数据类型支持的最大值')
        to_log('响应数据：\n' + str(data[0]))
        return {
            "code": "SUCCESS",
            "msg": "SUCCESS",
            "pay_summary": data[0]['pay_summary'],
            "total_pay_amt": data[0]['total_pay_amt'],
            "total_pay_count": data[0]['total_pay_count'],
            "transaction_detail": []
        }
    if bq_count == 2:
        to_log(str(bq_count) + '. 超过客户端所用数据类型支持的最大值时，客户端无cash')
        to_log('响应数据：\n' + str(data[1]))
        return {
            "code": "SUCCESS",
            "msg": "SUCCESS",
            "pay_summary": data[1]['pay_summary'],
            "total_pay_amt": data[1]['total_pay_amt'],
            "total_pay_count": data[1]['total_pay_count'],
            "transaction_detail":  []
        }
    if bq_count == 3:
        to_log(str(bq_count) + '. 边界最小值')
        to_log('响应数据：\n' + str(data[2]))
        return {
            "code": "SUCCESS",
            "msg": "SUCCESS",
            "pay_summary": data[2]['pay_summary'],
            "total_pay_amt": data[2]['total_pay_amt'],
            "total_pay_count": data[2]['total_pay_count'],
            "transaction_detail":  []
        }
    if bq_count == 4:
        to_log(str(bq_count) + '. 有效等价值')
        to_log('响应数据：\n' + str(data[3]))
        return {
            "code": "SUCCESS",
            "msg": "SUCCESS",
            "pay_summary": data[3]['pay_summary'],
            "total_pay_amt": data[3]['total_pay_amt'],
            "total_pay_count": data[3]['total_pay_count'],
            "transaction_detail":  []
        }
    if bq_count == 5:
        to_log(str(bq_count) + '. 无交易记录')
        to_log('响应数据：\n' + str(data[4]))
        return data[4]

    # 交易记录测试
    if bq_count > len(data):
        to_log('\n交易记录测试')
        return {
            "code": "SUCCESS",
            "msg": "SUCCESS",
            "transaction_detail": transaction_detail
        }


# 192.168.20.94
bottle.run(host='localhost', port=8886)

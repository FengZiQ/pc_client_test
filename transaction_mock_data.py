# coding=utf-8
import datetime

timeNow = datetime.datetime.now()
# 当前日期
today = timeNow.strftime('%Y%m%d%H%M%S')
# 昨天
yesterday = (timeNow - datetime.timedelta(days=1)).strftime('%Y%m%d%H%M%S')
# 二十天前
twentyDaysAgo = (timeNow - datetime.timedelta(days=20)).strftime('%Y%m%d%H%M%S')


data = [
    # 微信
    # 客户端所用数据类型支持的最大值
    {
        "buyer_pay_fee": 2147483647,
        "pay_fee": 2147483647,
        "pay_status": 2,
        "pay_type": "WXPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": today,
        "total_fee": 2147483647,
        "transaction_id": "4200000260201902193256608573"
    },
    # 最小金额
    {
        "buyer_pay_fee": 1,
        "pay_fee": 1,
        "pay_status": 2,
        "pay_type": "WXPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": today,
        "total_fee": 1,
        "transaction_id": "4200000260201902193256608573"
    },
    # 超过客户端所用数据类型支持的最大值
    {
        "buyer_pay_fee": 3147483647,
        "pay_fee": 3147483647,
        "pay_status": 2,
        "pay_type": "WXPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": today,
        "total_fee": 3147483647,
        "transaction_id": "4200000260201902193256608573"
    },
    # 其他等价金额
    {
        "buyer_pay_fee": 95333,
        "pay_fee": 95333,
        "pay_status": 2,
        "pay_type": "WXPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": today,
        "total_fee": 95333,
        "transaction_id": "4200000260201902193256608573"
    },
    # 昨天订单
    {
        "buyer_pay_fee": 95333,
        "pay_fee": 95333,
        "pay_status": 2,
        "pay_type": "WXPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": yesterday,
        "total_fee": 95333,
        "transaction_id": "4200000260201902193256608573"
    },
    {
        "buyer_pay_fee": 95333,
        "pay_fee": 95333,
        "pay_status": 2,
        "pay_type": "WXPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": yesterday,
        "total_fee": 95333,
        "transaction_id": "4200000260201902193256608573"
    },
    {
        "buyer_pay_fee": 95333,
        "pay_fee": 95333,
        "pay_status": 2,
        "pay_type": "WXPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": yesterday,
        "total_fee": 95333,
        "transaction_id": "4200000260201902193256608573"
    },
    # 二十天前的订单
    {
        "buyer_pay_fee": 95333,
        "pay_fee": 95333,
        "pay_status": 2,
        "pay_type": "WXPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": twentyDaysAgo,
        "total_fee": 95333,
        "transaction_id": "4200000260201902193256608573"
    },
    {
        "buyer_pay_fee": 95333,
        "pay_fee": 95333,
        "pay_status": 2,
        "pay_type": "WXPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": twentyDaysAgo,
        "total_fee": 95333,
        "transaction_id": "4200000260201902193256608573"
    },
    {
        "buyer_pay_fee": 95333,
        "pay_fee": 95333,
        "pay_status": 2,
        "pay_type": "WXPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": twentyDaysAgo,
        "total_fee": 95333,
        "transaction_id": "4200000260201902193256608573"
    },
    # 支付宝
    # 客户端所用数据类型支持的最大值
    {
        "buyer_pay_fee": 2147483647,
        "pay_fee": 2147483647,
        "pay_status": 2,
        "pay_type": "ALIPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": today,
        "total_fee": 2147483647,
        "transaction_id": "4200000260201902193256608573"
    },
    # 最小金额
    {
        "buyer_pay_fee": 1,
        "pay_fee": 1,
        "pay_status": 2,
        "pay_type": "ALIPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": today,
        "total_fee": 1,
        "transaction_id": "4200000260201902193256608573"
    },
    # 超过客户端所用数据类型支持的最大值
    {
        "buyer_pay_fee": 3147483647,
        "pay_fee": 3147483647,
        "pay_status": 2,
        "pay_type": "ALIPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": today,
        "total_fee": 3147483647,
        "transaction_id": "4200000260201902193256608573"
    },
    # 其他等价金额
    {
        "buyer_pay_fee": 95333,
        "pay_fee": 95333,
        "pay_status": 2,
        "pay_type": "ALIPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": today,
        "total_fee": 95333,
        "transaction_id": "4200000260201902193256608573"
    },
    # 昨天订单
    {
        "buyer_pay_fee": 95333,
        "pay_fee": 95333,
        "pay_status": 2,
        "pay_type": "ALIPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": yesterday,
        "total_fee": 95333,
        "transaction_id": "4200000260201902193256608573"
    },
    {
        "buyer_pay_fee": 95333,
        "pay_fee": 95333,
        "pay_status": 2,
        "pay_type": "ALIPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": yesterday,
        "total_fee": 95333,
        "transaction_id": "4200000260201902193256608573"
    },
    {
        "buyer_pay_fee": 95333,
        "pay_fee": 95333,
        "pay_status": 2,
        "pay_type": "ALIPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": yesterday,
        "total_fee": 95333,
        "transaction_id": "4200000260201902193256608573"
    },
    # 二十天前的订单
    {
        "buyer_pay_fee": 95333,
        "pay_fee": 95333,
        "pay_status": 2,
        "pay_type": "ALIPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": twentyDaysAgo,
        "total_fee": 95333,
        "transaction_id": "4200000260201902193256608573"
    },
    {
        "buyer_pay_fee": 95333,
        "pay_fee": 95333,
        "pay_status": 2,
        "pay_type": "ALIPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": twentyDaysAgo,
        "total_fee": 95333,
        "transaction_id": "4200000260201902193256608573"
    },
    {
        "buyer_pay_fee": 95333,
        "pay_fee": 95333,
        "pay_status": 2,
        "pay_type": "ALIPAY",
        "refund_fee": 0,
        "refund_status": 0,
        "time_end": twentyDaysAgo,
        "total_fee": 95333,
        "transaction_id": "4200000260201902193256608573"
    }
]

transaction_detail = data*1000

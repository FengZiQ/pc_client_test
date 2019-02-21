# coding=utf-8

data = [
    # 客户端所用数据类型支持的最大值
    {
        "pay_summary": [
            {
                "pay_type": "WXPAY",
                "total_pay_count": 2147483647,
                "total_pay_fee": 2147483647
            },
            {
                "pay_type": "ALIPAY",
                "total_pay_count": 2147483647,
                "total_pay_fee": 2147483647
            }
        ],
        "total_pay_amt": 2147483647,
        "total_pay_count": 2147483647
    },
    # 超过客户端所用数据类型支持的最大值时，客户端无cash
    {
        "pay_summary": [
            {
                "pay_type": "WXPAY",
                "total_pay_count": 3147483647,
                "total_pay_fee": 3147483647
            },
            {
                "pay_type": "ALIPAY",
                "total_pay_count": 3147483647,
                "total_pay_fee": 3147483647
            }
        ],
        "total_pay_amt": 3147483647,
        "total_pay_count": 3147483647
    },
    # 边界最小值
    {
        "pay_summary": [
            {
                "pay_type": "WXPAY",
                "total_pay_count": 1,
                "total_pay_fee": 1
            },
            {
                "pay_type": "ALIPAY",
                "total_pay_count": 1,
                "total_pay_fee": 1
            }
        ],
        "total_pay_amt": 2,
        "total_pay_count": 2
    },
    # 有效等价值
    {
        "pay_summary": [
            {
                "pay_type": "WXPAY",
                "total_pay_count": 99999,
                "total_pay_fee": 9999900
            },
            {
                "pay_type": "ALIPAY",
                "total_pay_count": 99999,
                "total_pay_fee": 9999900
            }
        ],
        "total_pay_amt": 19999800,
        "total_pay_count": 199998
    },
    # 无交易记录
    {
        "code": "SUCCESS",
        "msg": "SUCCESS",
        "transaction_detail": []
    }
]


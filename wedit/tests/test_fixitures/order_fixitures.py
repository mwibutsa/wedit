query_orders = '''
    orders {
        id
        owner
    }
'''


order_mutation = '''
    mutation {{
        createOrder(
            orderTitle: "{}",
            orderFile:"{}",
            orderSummary: "{}",
            descriptionFile:"{}"
        ) {{
        orderTitle
        orderFile
        orderSummary
        descriptionFile
        owner
        }}
    }}
'''

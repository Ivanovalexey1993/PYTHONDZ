import view
import menu
import logger

def button_click():
    value_a = view.get_value()
    oper = view.get_operation()
    value_b = view.get_value()
    func = menu.dict_arith[oper]
    func.init(value_a, value_b)
    result = func.do_it()
    view.get_result(result)
    operation = menu.dict_log[oper]
    logger.get_log(result, operation)
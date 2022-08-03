import api
import overheads
import cash_on_hand
import profit_loss

def main():
    forex = api.api_function()
    overheads.overheads_function(forex)
    cash_on_hand.coh_function(forex)
    profit_loss.profitloss_function(forex)

main()
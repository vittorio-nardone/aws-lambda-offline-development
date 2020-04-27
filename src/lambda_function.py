import logging
import PIL

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    ## Event contents
    logger.info('## EVENT')
    logger.info(event)
    
    ## SQS Event processing sample
    Results = []
    for r in event['Records']:
        body = r['body']
        addenda = [int(body[k]) for k in body]
        Results.append(sum(addenda))   

    logger.info('## RESULTS')
    [logger.info('Sum is {}'.format(r)) for r in Results] 

    ## Required package sample
    logger.info('## PILLOW VERSION')
    logger.info(PIL.__version__)

    ## Lambda return sample
    return { 
        'return_message' : 'All the best for you'
    }  
import requests

from opencensus.ext.azure.trace_exporter import AzureExporter
# from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace.tracer import Tracer

# TODO: replace the all-zero GUID with your instrumentation key.
tracer = Tracer(
    exporter=AzureExporter(
        instrumentation_key='<ENTER_INSTRUMENTATION_KEY>',
    ),
)

def printResponse(res):
    print(res)


def makehttpReq():
    with tracer.span(name='span1'):
        with tracer.span(name='span1_child1'):
            response = requests.get(
                'http://localhost:8080/tickets/dummycontent-for-avail')
        with tracer.span(name='span1_child2'):
            printResponse(response._content)
    with tracer.span(name='span2'):
        with tracer.span(name='span2_child1'):
            response = requests.get(
                'http://localhost:8080/tickets/listHeaders')

def main():
    makehttpReq()


if __name__ == "__main__":
    main()

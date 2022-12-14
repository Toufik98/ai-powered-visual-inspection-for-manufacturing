# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rgb_image_pb2 as rgb__image__pb2


class Predict_serviceStub(object):
    """Service to predict the label of an image
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Predict = channel.unary_unary(
                '/ai_powered_visual_inspection_for_manifacturing.Predict_service/Predict',
                request_serializer=rgb__image__pb2.RGB_image.SerializeToString,
                response_deserializer=rgb__image__pb2.Predicted.FromString,
                )


class Predict_serviceServicer(object):
    """Service to predict the label of an image
    """

    def Predict(self, request, context):
        """Predict the label of an image
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Predict_serviceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Predict': grpc.unary_unary_rpc_method_handler(
                    servicer.Predict,
                    request_deserializer=rgb__image__pb2.RGB_image.FromString,
                    response_serializer=rgb__image__pb2.Predicted.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ai_powered_visual_inspection_for_manifacturing.Predict_service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Predict_service(object):
    """Service to predict the label of an image
    """

    @staticmethod
    def Predict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_powered_visual_inspection_for_manifacturing.Predict_service/Predict',
            rgb__image__pb2.RGB_image.SerializeToString,
            rgb__image__pb2.Predicted.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

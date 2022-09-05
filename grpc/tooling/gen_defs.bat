@echo off

rmdir /S ..\grpc_frontend\protodefs
mkdir ..\grpc_frontend\protodefs

.\protoc.exe ..\grpc_backend\Protos\greet.proto --proto_path=..\grpc_backend\Protos --js_out=import_style=commonjs:..\grpc_frontend\protodefs
.\protoc.exe ..\grpc_backend\Protos\greet.proto --proto_path=..\grpc_backend\Protos --grpc-web_out=import_style=commonjs,mode=grpcwebtext:..\grpc_frontend\protodefs
@echo off

cd .\tools
rmdir /S /Q ..\protodefs
mkdir ..\protodefs

.\protoc.exe ..\..\protos\greet.proto --proto_path=..\..\protos --js_out=import_style=commonjs:..\protodefs
.\protoc.exe ..\..\protos\greet.proto --proto_path=..\..\protos --grpc-web_out=import_style=commonjs,mode=grpcwebtext:..\protodefs

.\protoc.exe ..\..\protos\chat.proto --proto_path=..\..\protos --js_out=import_style=commonjs:..\protodefs
.\protoc.exe ..\..\protos\chat.proto --proto_path=..\..\protos --grpc-web_out=import_style=commonjs,mode=grpcwebtext:..\protodefs
ID=27dec2018
buildImage:
	docker build -t ijal:$(ID) -f Dockerfile .

bash:
	docker run -ti --rm -p 60043:8050 ijal:$(ID) bash



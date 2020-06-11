FROM python:3.6
#WORKDIR /dataintegratie
ADD vcf_to_mongodb.py /
# RUN apk add --no-cache gcc musl-dev linux-headers
#COPY ../install_and_deploy_mongodb.sh instal_and_deploy_mongodb.sh
COPY gnomad.exomes.r2.1.1.sites.13.vcf gnomad.exomes.r2.1.1.sites.13.vcf
#COPY ../requirements.txt requirements.txt
#RUN sh install_and_deploy_mongodb.sh
RUN pip install pymongo
RUN pip install PyVCF


ENV PATH " $PATH:/media/carlijnfransen/HD_CarlijnFransen/BIN-1920/gnomad.exomes.r2.1.1.sites.13.vcf"

EXPOSE 5000
CMD ["python" ,"vcf_to_mongodb.py"  ]



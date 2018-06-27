# Travis windows encoding issue

## My error:

```
$ openssl aes-256-cbc -K $encrypted_e59edd753e7a_key -iv $encrypted_e59edd753e7a_iv -in credentials.tar.gz.enc -out credentials.tar.gz -d
bad decrypt
140265468671648:error:0606506D:digital envelope routines:EVP_DecryptFinal_ex:wrong final block length:evp_enc.c:532:
The command "openssl aes-256-cbc -K $encrypted_e59edd753e7a_key -iv $encrypted_e59edd753e7a_iv -in credentials.tar.gz.enc -out credentials.tar.gz -d" failed and exited with 1 during .
```

## Ideas of how to solve

### a - Run the encryption manually

- Have to rerun the `travis encrypt-file credentials.tar.gz --add` line manually with something like:
```
$ travis encrypt super_secret_password=ahduQu9ushou0Roh --add
$ openssl aes-256-cbc -k "ahduQu9ushou0Roh" -in super_secret.txt -out super_secret.txt.enc
(keep in mind to replace the password with the proper value)
```
(as seen [here](https://docs.travis-ci.com/user/encrypting-files/#Using-OpenSSL)


### b - Run the encryptian on a linux & send the file back

#### Step 1 - scp the .tar.gz file to your linux instance

```
scp -i ~/Dropbox/Admin/aws-g2-key-ncal.pem credentials.tar.gz ubuntu@54.183.251.127:~/
```

#### Step 2 - ssh to the instance, check the file is there

```
ssh -i ~/Dropbox/Admin/aws-g2-key-ncal.pem ubuntu@54.183.251.127
```

#### Step 3 (maybe) - Install ruby, install travis

I had to install ruby on my box in order to install the travis cli. That involved adding the brightbox repository to my apt-get

```
sudo apt-add-repository ppa:brightbox/ruby-ng
sudo apt-get update
sudo apt-get install ruby2.3 ruby2.3-dev
sudo gem install travis
```

#### Step 4 - Login to travis

```
travis login --org
```

#### Step 5 - Run the encryption

```
travis encrypt-file -r playoffs-widget-app credentials.tar.gz
```

#### Step 6 - Exit the instance & copy the file back down to your local

```
exit
scp -i ~/Dropbox/Admin/aws-g2-key-ncal.pem ubuntu@54.183.251.127:~/credentials.tar.gz.enc  .
``` 
















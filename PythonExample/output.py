import requests, json

print requests.get("http://www.threatcrowd.org/searchApi/v2/domain/report/", {"domain": "aoldaily.com"}).text



Result:

{
   "response_code":"1",
   "resolutions":[
      {
         "last_resolved":"2015-02-17",
         "domain":"tvgate.rocks"
      },
     ... [More]
   ],
   "hashes":[
      "003f0ed24b5f70ddc7c6e80f9c4dac73",
     ... [More]
   ],
   "references":[
      ""
   ],
   "permalink":"https:\/\/www.threatcrowd.org\/ip.php?ip=188.40.75.132"
}


{
   "response_code":"1",
   "hashes":[
      "321c1d36c16833477ada58ccfa012c6e",
      "ec83d8379140396c8a18368af9d18421",
      "38e0e7d95ef07f6ae514b1c883884c9b",
      "c3f8b1ce2f9dc658e4a9ff198aabeb52",
      "37aacb043222f814ef5013ab2bd6d820",
      "9c6c697f4fbe5cc3c5c8900cbb390ed1",
      "261a336ac5f9ffd6b6f6629d71c694d7",
      "27d74947440dfcc91cb48dd2caa97375",
      "56e11c88636ae745bc5b494a3ed10c21",
      "4c1ad55784314eaa686e7f356b176e44",
      "93cc00543b369a24c4db031b0411c65a",
      "1e728ba8947b8913807562ff7f010a1f",
      "2b88f6504fd54bbc454031f255a97cdf",
      "169288437888fe819abeb0499e58ec22",
      "f8a370de9233d27fed89ce7a7f7a03d1",
      "6622918d92a44e67175f7aeb3fcb5a05",
      "a5f60f1fa6e80fdbe82eff51c1245460",
      "9962800c103eee89d140de26c3ee20e6",
      "69b7c08a2e149ceb4f6ff9bd61f14290",
      "b5697ceba684362b82a8f4cbcf3ab201",
      "7c6722e3d52a578a080ac35de81c2e8e",
      "2782c6cca0fad33d896feef4ec92f24b",
      "dc78d92d10b486db9b610920959107e1",
      "1c87f3704911d94d89fcf4f4c05c1897",
      "1abbd53263fffaa8d97ccc67f5b3dea1",
      "876f24c4102a4e911ab77ee328643dd2",
      "5aa8efccaf6955e6949977a96c2cb0c2",
      "64590646ab74325ee2ad480ef5a18307",
      "642b12cdda124e1f70b548d126600f98",
      "d9ab2b14e9b2f1d78c117fdb1bf0601e",
      "637c9cd17fc8f42910d536b46ed3b445",
      "2743b6bece1c5b6c30747da080c26673",
      "3745095be9859492fc9975c66192310d",
      "be2fd18964ad1e550d4c5f33bb6d0766",
      "27b2ef2fa1c46239b7da08e61533d3c9",
      "cc7b091b94c4f0641b180417b017fec2",
      "405386b0fd12bc0defc9e4e4f4d2ad05",
      "1ed0137d6b78f00f2ed3945d84d626aa",
      "0bf5e206b4058887633ad8a3e7e0bdea",
      "ef9d8cd06de03bd5f07b01c1cce9761f",
      "c2fd460d5734dac2baf533576804c85e",
      "fa816236701d93b09ea9e883b449fa33",
      "62898b77bd9e8e286d6bc760f3e28981",
      "4f92b6c9c55142ee562e8237ce1436a2",
      "917a31528c38e0cec2a3e10210235625",
      "01b16dff4a49a1f368c547e3a7bed9ce",
      "dc9207ad7e0d1678e96c89ac1bf19354",
      "22201573c8831f01293c611f8d851bf1",
      "46869e9c38f8b6a9517b41d7378399b9",
      "c557b6dc0edab783781fd9312f6886c3"
   ],
   "references":[

   ],
   "permalink":"https:\/\/www.threatcrowd.org\/listMalware.php?antivirus=plugx"
}
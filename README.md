# Usando Stable Diffusion con Amazon Bedrock

Esta aplicación esta basada en el post original:
[Quickly build Generative AI applications with Amazon Bedrock](https://community.aws/content/2ddby9SeCKALvSz0CWUtx4Q4fPX/amazon-bedrock-quick-start)

## Permisos para Amazon Bedrock

Para el uso de Amazon Bedrock asegurar que se cuenta agregada la política de permisos: **AmazonBedrockFullAccess**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "BedrockAll",
      "Effect": "Allow",
      "Action": ["bedrock:*"],
      "Resource": "*"
    },
    {
      "Sid": "DescribeKey",
      "Effect": "Allow",
      "Action": ["kms:DescribeKey"],
      "Resource": "arn:*:kms:*:::*"
    },
    {
      "Sid": "APIsWithAllResourceAccess",
      "Effect": "Allow",
      "Action": [
        "iam:ListRoles",
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups"
      ],
      "Resource": "*"
    },
    {
      "Sid": "PassRoleToBedrock",
      "Effect": "Allow",
      "Action": ["iam:PassRole"],
      "Resource": "arn:aws:iam::*:role/*AmazonBedrock*",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": ["bedrock.amazonaws.com"]
        }
      }
    }
  ]
}
```

## Presets

Los presets parametrizados dentro de la app permiten generar diferentes tipos de imagenes de acuerdo con el estilo seleccionado.

```python
sd_presets: list = [
    "None",
    "3d-model",
    "analog-film",
    "anime",
    "cinematic",
    "fantasy-art",
    "comic-book",
    "photographic",
    "digital-art",
    "lowpoly",
    "craft-clay",
    "isometric",
    "pixel-art",
    "enhance",
]
```

## Ejecutar la app

Para ejecutar la aplicación se debe ejecutar el siguiente comando:

```bash
streamlit run stunning_images.py
```

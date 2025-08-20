# Express con Prisma y Typescript

## Creación del proyecto

```bash
mkdir express_prisma
cd express_prisma
npm init -y
```

## Instalación de las dependencias

```bash
npm install express @prisma/client
npm install -D typescript ts-node-dev prisma @types/express
```

## Configuración de typescript

```bash
npx tsc --init
```

```json
{
  "compilerOptions": {
    "module": "commonjs",
    "target": "esnext",
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "noUnusedLocals": true,
    "noUnusedParameters": false,
    "noFallthroughCasesInSwitch": true,
    "resolveJsonModule": true,
    "strict": true,
    "outDir": "./build"
  },
  "include": ["**/*.ts"],
  "exclude": ["node_modules", "build"]
}
```

## Package.json

```json
{
  "name": "express_prisma",
  "version": "1.0.0",
  "description": "```bash\r mkdir express_prisma\r cd express_prisma\r npm init -y\r ```",
  "main": "index.js",
  "scripts": {
    "dev": "ts-node-dev src/app.ts",
    "build": "tsc",
    "start": "node build/app.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "type": "commonjs",
  "dependencies": {
    "@prisma/client": "^6.14.0",
    "express": "^5.1.0"
  },
  "devDependencies": {
    "@types/express": "^5.0.3",
    "prisma": "^6.14.0",
    "ts-node-dev": "^2.0.0",
    "typescript": "^5.9.2"
  }
}
```

## Configuración de Prisma

```bash
npx prisma init
```
# My Node API

This project is a simple Node.js API that fetches address information based on a provided postal code (CEP) using the VIA CEP service.

## Project Structure

```
my-node-api
├── src
│   ├── app.js
│   ├── routes
│   │   └── address.js
│   ├── controllers
│   │   └── addressController.js
│   └── services
│       └── viaCepService.js
├── package.json
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd my-node-api
   ```

3. Install the dependencies:
   ```
   npm install
   ```

## Usage

1. Start the server:
   ```
   node src/app.js
   ```

2. Make a GET request to fetch an address by postal code (CEP):
   ```
   GET http://localhost:3000/address/{cep}
   ```
   Replace `{cep}` with the desired postal code.

## Example

To fetch the address for the postal code 01001-000, you would make a request to:
```
http://localhost:3000/address/01001-000
```

## License

This project is licensed under the MIT License.
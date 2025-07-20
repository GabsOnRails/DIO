const express = require('express');
const AddressController = require('../controllers/addressController');

const router = express.Router();
const addressController = new AddressController();

router.get('/:cep', addressController.getAddressByCep.bind(addressController));

module.exports = router;
const fetchAddressByCep = require('../services/viaCepService');

class AddressController {
    async getAddressByCep(req, res) {
        const { cep } = req.params;
        try {
            const address = await fetchAddressByCep(cep);
            if (!address) {
                return res.status(404).json({ message: 'Address not found' });
            }
            res.json(address);
        } catch (error) {
            res.status(500).json({ message: 'Error fetching address', error: error.message });
        }
    }
}

module.exports = AddressController;
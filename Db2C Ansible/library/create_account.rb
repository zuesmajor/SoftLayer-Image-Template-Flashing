require 'softlayer_api'
require 'json'

# Credentials to the API are read from a configuration file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44


$SL_API_USERNAME = "ryanpa_573505";
$SL_API_KEY = "Change me";

client = SoftLayer::Client.new;

account_service = client['Account'];
brand_service = client['Brand'];

brand = account_service.getBrand();

# puts JSON.pretty_generate(brand);

cust_account = {
  brandId: brand['id'].to_i, # change me loops through and grabs the ID
  allowedPptpVpnQuantity: 1,
  claimedTaxExemptTxFlag: false,
  companyName: 'IBM', # change me
  isReseller: 0,
  lateFeeProtectionFlag: true,
  firstName: 'Asim', # change me
  lastName: 'Singh', # change me
  email: 'avsingh@us.ibm.com', # change me
  officePhone: '4083340551', # change me
  address1: '555 Bailey Ave', # change me
  city: 'San Jose', # change me
  state: 'CA', # change me
  postalCode: '95141', # change me
  country: 'US' # change me
}

  result = brand_service.createCustomerAccount(cust_account);
  puts JSON.pretty_generate(result);



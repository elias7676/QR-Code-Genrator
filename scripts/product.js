function getFromInput() {
  return {
    //sms
    "phone_number": getValue("phone_number"),
    "message": getValue("message"),
    //vcard
    "firstName": getValue("firstName"),
    "lastName": getValue("lastName"),
    "phone": getValue("phone"),
    "email": getValue("email"),
    //location
    "latitude": getValue("latitude"),
    "longitude": getValue("longitude"),
    //event
    "summary":getValue("summary"),
    "description":getValue("description"),
    "location":getValue("location"),
    "start":getValue("start"),
    "end":getValue("end"),
    //wifi
    "ssid":getValue("ssid"),
    "password":getValue("password"),
    //url
    "url":getValue("url"),
    "linkedin":getValue("linkedin"),
    "marketplace":getValue("marketplace"),
    "telegram":getValue("telegram"),
    "tiktok":getValue("tiktok")

    //"sellStartDate": new Date(getValue("sellStartDate"))
  };
}

function setInput(product) {
  // setValue("productID", product.productID);
  // setValue("name", product.name);
  // setValue("productNumber", product.productNumber);
  // setValue("color", product.color);
  // setValue("standardCost", product.standardCost);
  // setValue("listPrice", product.listPrice);
  // setValue("sellStartDate", product.sellStartDate);
}

function clearInput() {
  setValue("phone_number", "0");
  setValue("message", "0");
  setValue("firstName", "0");
  setValue("lastName", "0");
  setValue("phone", "0");
  setValue("email", "0");
  setValue("longitude", "0");
  setValue("latitude", "0");
  setValue("summary", "0");
  setValue("description", "0");
  setValue("location", "0");
  setValue("start", "0");
  setValue("end", "0");
  setValue("ssid", "0");
  setValue("password", "0");
  setValue("url", "0");
  setValue("linkedin", "0");
  setValue("marketplace", "0");
  setValue("telegram", "0");
  setValue("tiktok", "0");
  //setValue("sellStartDate", new Date().toLocaleDateString());
}

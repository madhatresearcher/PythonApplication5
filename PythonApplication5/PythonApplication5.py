amazon_cart=['laptop','shoes','phone',6,'trolley'];
print('enter the extra items to buy:');
item1=input();
item2=input();
item3=input();
item4=input();
item5=input();
newegg_cart=[item1,item2,item3,item4,item5];
print(newegg_cart);
print(len(newegg_cart));
print(newegg_cart[0:len(newegg_cart)]);
print(type(item1));
newegg_cart[0]='brakes';
print(newegg_cart);
newegg_cart[4]='shoe pads';
newegg_cart[3]=90;
newegg_cart=newegg_cart+['snakes'];
print(len(newegg_cart));
newegg_cart=newegg_cart+[6];
newegg_cart[6]=input();
print(newegg_cart);
print(len(newegg_cart));
newegg_cart=newegg_cart+[7];
print(len(newegg_cart));
print(newegg_cart);
newegg_cart[7]=input();
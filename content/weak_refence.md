title: 弱引用
Date: 2017-06-28 20:30
Category: python

弱引用不会增加对象的引用数量，引用的目标对象称为所指对象，弱引用在缓存应用中很有用，因为我

们不想仅因为被缓存引用着而始终保存着缓存对象。

基本的list和dict实例不会做为弱引用的目标，但他们的子类可以，set可以作为弱引用所指对象，int和

tuple不可以作为弱引用的所指对象，它们的子类也不可以。
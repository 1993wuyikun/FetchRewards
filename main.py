# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from mongoengine import *
from ReceiptMongo import Receipt, User, Brand
from SQLTable import ReceiptSQL, ItemSQL, ReceiptItemSQL, UserSQL, BrandSQL
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, inspect, DateTime, Float, Boolean, ForeignKey, exists


def print_hi(name):
    connect('myMongoDb', host='127.0.0.1', port=27017)

    # 初始化数据库连接:
    engine = create_engine("mysql+pymysql://root:Yhm95471963#@localhost:3306/test", echo=True)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    # 创建session对象:
    session = DBSession()
    metadata = MetaData(engine)

    if not inspect(engine).has_table(ReceiptItemSQL):
        Table(
            'receipt_item', metadata,
            Column('receipt_id', String(28), ForeignKey('receipt.id')),
            Column('item_id', String(28), ForeignKey('item.id'))

        )

    if not inspect(engine).has_table(ReceiptSQL):
        receipts = Table(
            'receipt', metadata,
            Column('id', String(28), primary_key=True),
            Column('userId', String(50)),
            Column('bonusPointsEarned', Integer),
            Column('bonusPointsEarnedReason', String(1000)),
            Column('createDate', DateTime),
            Column('dateScanned', DateTime),
            Column('finishedDate', DateTime),
            Column('modifyDate', DateTime),
            Column('pointsAwardedDate', DateTime),
            Column('pointsEarned', Integer),
            Column('purchaseDate', DateTime),
            Column('purchasedItemCount', Integer),
            Column('rewardsReceiptStatus', String(50)),
            Column('totalSpent', Float),
            Column('userId', String(28)),
        )

    if not inspect(engine).has_table(ItemSQL):
        items = Table(
            'item', metadata,
            Column('id', String(28), primary_key=True),
            Column('description', String(1000)),
            Column('finalPrice', Float),
            Column('itemPrice', Float),
            Column('needsFetchReview', Boolean),
            Column('partnerItemId', String(50)),
            Column('pointsPayerId', String(50)),
            Column('rewardsProductPartnerId', String(50)),
            Column('pointsNotAwardedReason', String(1000)),
            Column('needsFetchReviewReason', String(1000)),
            Column('userFlaggedDescription', String(1000)),
            Column('rewardsGroup', String(1000)),
            Column('originalMetaBriteBarcode', String(50)),
            Column('brandCode', String(50)),
            Column('competitorRewardsGroup', String(1000)),
            Column('originalReceiptItemText', String(1000)),
            Column('discountedItemPrice', Float),
            Column('itemNumber', String(50)),
            Column('targetPrice', Float),
            Column('pointsEarned', Integer),
            Column('competitiveProduct', Boolean),
            Column('originalMetaBriteItemPrice', Float),
            Column('originalFinalPrice', Float),
            Column('deleted', Boolean),
            Column('priceAfterCoupon', Float),
            Column('metabriteCampaignId', String(1000)),
            Column('originalMetaBriteQuantityPurchased', Integer),
            Column('originalMetaBriteDescription', String(1000)),
            Column('preventTargetGapPoints', Boolean),
            Column('quantityPurchased', Integer),
            Column('userFlaggedBarcode', String(50)),
            Column('userFlaggedNewItem', Boolean),
            Column('userFlaggedPrice', Float),
            Column('userFlaggedQuantity', Integer),
        )

    if not inspect(engine).has_table(UserSQL):
        Table(
            'user', metadata,
            Column('id', String(28), primary_key=True),
            Column('active', String(1000)),
            Column('createdDate', DateTime),
            Column('lastLogin', DateTime),
            Column('role', String(1000)),
            Column('signUpSource', String(1000)),
            Column('state', String(28))

        )

    if not inspect(engine).has_table(BrandSQL):
        Table(
            'brand', metadata,
            Column('id', String(28), primary_key=True),
            Column('barcode', String(28)),
            Column('brandCode', String(100)),
            Column('pointsPayerId', String(28)),
            Column('category', String(28)),
            Column('categoryCode', String(100)),
            Column('name', String(1000)),
            Column('topBrand', String(100))

        )
    metadata.create_all(engine)

    for user in User.objects:
        new_user = UserSQL(id=str(user.id),
                           active=user.active,
                           createdDate=user.createdDate,
                           lastLogin=user.lastLogin,
                           role=user.role,
                           signUpSource=user.signUpSource,
                           state=user.state)

        session.add(new_user)

    for receipt in Receipt.objects:
        new_receipt = ReceiptSQL(id=str(receipt.id),
                                 bonusPointsEarned=receipt.bonusPointsEarned,
                                 bonusPointsEarnedReason=receipt.bonusPointsEarnedReason,
                                 createDate=receipt.createDate,
                                 dateScanned=receipt.dateScanned,
                                 finishedDate=receipt.finishedDate,
                                 modifyDate=receipt.modifyDate,
                                 pointsAwardedDate=receipt.pointsAwardedDate,
                                 pointsEarned=receipt.pointsEarned,
                                 purchaseDate=receipt.purchaseDate,
                                 purchasedItemCount=receipt.purchasedItemCount,
                                 rewardsReceiptStatus=receipt.rewardsReceiptStatus,
                                 totalSpent=receipt.totalSpent,
                                 userId=receipt.userId)
        # 添加到session:
        session.add(new_receipt)
        for rewardsReceiptItem in receipt.rewardsReceiptItemList:
            if rewardsReceiptItem.barcode:

                it_exists = session.query(exists().where(ItemSQL.id == rewardsReceiptItem.barcode)).scalar()
                if not it_exists:
                    new_item = ItemSQL(id=rewardsReceiptItem.barcode,
                                       description=rewardsReceiptItem.description,
                                       finalPrice=rewardsReceiptItem.finalPrice,
                                       itemPrice=rewardsReceiptItem.itemPrice,
                                       needsFetchReview=rewardsReceiptItem.needsFetchReview,
                                       partnerItemId=rewardsReceiptItem.partnerItemId,
                                       pointsPayerId=rewardsReceiptItem.pointsPayerId,
                                       rewardsProductPartnerId=rewardsReceiptItem.rewardsProductPartnerId,
                                       pointsNotAwardedReason=rewardsReceiptItem.pointsNotAwardedReason,
                                       needsFetchReviewReason=rewardsReceiptItem.needsFetchReviewReason,
                                       userFlaggedDescription=rewardsReceiptItem.description,
                                       rewardsGroup=rewardsReceiptItem.rewardsGroup,
                                       originalMetaBriteBarcode=rewardsReceiptItem.originalMetaBriteBarcode,
                                       brandCode=rewardsReceiptItem.brandCode,
                                       competitorRewardsGroup=rewardsReceiptItem.competitorRewardsGroup,
                                       originalReceiptItemText=rewardsReceiptItem.originalReceiptItemText,
                                       discountedItemPrice=rewardsReceiptItem.discountedItemPrice,
                                       itemNumber=rewardsReceiptItem.itemNumber,
                                       targetPrice=rewardsReceiptItem.targetPrice,
                                       pointsEarned=rewardsReceiptItem.pointsEarned,
                                       competitiveProduct=rewardsReceiptItem.competitiveProduct,
                                       originalMetaBriteItemPrice=rewardsReceiptItem.originalMetaBriteItemPrice,
                                       originalFinalPrice=rewardsReceiptItem.originalFinalPrice,
                                       deleted=rewardsReceiptItem.deleted,
                                       priceAfterCoupon=rewardsReceiptItem.priceAfterCoupon,
                                       metabriteCampaignId=rewardsReceiptItem.metabriteCampaignId,
                                       originalMetaBriteQuantityPurchased=rewardsReceiptItem.originalMetaBriteQuantityPurchased,
                                       originalMetaBriteDescription=rewardsReceiptItem.originalMetaBriteDescription,
                                       preventTargetGapPoints=rewardsReceiptItem.preventTargetGapPoints,
                                       quantityPurchased=rewardsReceiptItem.quantityPurchased,
                                       userFlaggedBarcode=rewardsReceiptItem.userFlaggedBarcode,
                                       userFlaggedNewItem=rewardsReceiptItem.userFlaggedNewItem,
                                       userFlaggedPrice=rewardsReceiptItem.userFlaggedPrice,
                                       userFlaggedQuantity=rewardsReceiptItem.userFlaggedQuantity)
                    session.add(new_item)
                new_receipt_item = ReceiptItemSQL(receipt_id=str(receipt.id),
                                                  item_id=rewardsReceiptItem.barcode)
                session.add(new_receipt_item)

    for brand in Brand.objects:
        new_brand = BrandSQL(id=str(brand.id),
                             barcode=brand.barcode,
                             brandCode=brand.brandCode,
                             category=brand.category,
                             categoryCode=brand.categoryCode,
                             pointsPayerId=str(brand.cpg.id),
                             name=brand.name,
                             topBrand=brand.topBrand)

        session.add(new_brand)


    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

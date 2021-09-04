from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ReceiptItemSQL(Base):
    __tablename__ = 'receipt_item'
    receipt_id = Column(String(28), ForeignKey('receipt.id'), primary_key=True)
    item_id = Column(String(28), ForeignKey('item.id'), primary_key=True)

    item = relationship('ItemSQL')
    receipt = relationship('ReceiptSQL')


class ReceiptSQL(Base):

    __tablename__ = 'receipt'

    id = Column(String(28), primary_key=True)
    bonusPointsEarned = Column(Integer)
    bonusPointsEarnedReason = Column(Text(1000))
    createDate = Column(DateTime)
    dateScanned = Column(DateTime)
    finishedDate = Column(DateTime)
    modifyDate = Column(DateTime)
    pointsAwardedDate = Column(DateTime)
    pointsEarned = Column(String(28))
    purchaseDate = Column(DateTime)
    purchasedItemCount = Column(Integer)
    rewardsReceiptStatus = Column(String(20))
    totalSpent = Column(Float)
    userId = Column(String(28))


class ItemSQL(Base):

    __tablename__ = 'item'

    id = Column(String(28), primary_key=True)
    description = Column(Text(1000))
    finalPrice = Column(Float)
    itemPrice = Column(Float)
    needsFetchReview = Column(Boolean)
    partnerItemId = Column(String(50))
    pointsPayerId = Column(String(50))
    rewardsProductPartnerId = Column(String(50))
    pointsNotAwardedReason = Column(Text(1000))
    needsFetchReviewReason = Column(Text(1000))
    userFlaggedDescription = Column(Text(1000))
    rewardsGroup = Column(Text(1000))
    originalMetaBriteBarcode = Column(String(50))
    brandCode = Column(String(50))
    competitorRewardsGroup = Column(Text(1000))
    originalReceiptItemText = Column(Text(1000))
    discountedItemPrice = Column(Float)
    itemNumber = Column(String(50))
    targetPrice = Column(Float)
    pointsEarned = Column(Integer)
    competitiveProduct = Column(Boolean)
    originalMetaBriteItemPrice = Column(Float)
    originalFinalPrice = Column(Float)
    deleted = Column(Boolean)
    priceAfterCoupon = Column(Float)
    metabriteCampaignId = Column(Text(1000))
    originalMetaBriteQuantityPurchased = Column(Integer)
    originalMetaBriteDescription = Column(Text(1000))
    preventTargetGapPoints = Column(Boolean)
    quantityPurchased = Column(Integer)
    userFlaggedBarcode = Column(String(50))
    userFlaggedNewItem = Column(Boolean)
    userFlaggedPrice = Column(Float)
    userFlaggedQuantity = Column(Integer)


class UserSQL(Base):

    __tablename__ = "user"

    id = Column(String(28), primary_key=True)
    active = Column(Text(100))
    createdDate = Column(DateTime)
    lastLogin = Column(DateTime)
    role = Column(Text(100))
    signUpSource = Column(Text(100))
    state = Column(String(28))


class BrandSQL(Base):

    __tablename__ = "brand"

    id = Column(String(28), primary_key=True)
    barcode = Column(String(28))
    brandCode = Column(String(100))
    pointsPayerId = Column(String(28))
    category = Column(String(28))
    categoryCode = Column(String(100))
    name = Column(Text(1000))
    topBrand = Column(String(100))




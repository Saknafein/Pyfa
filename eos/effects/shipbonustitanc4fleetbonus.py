# shipBonusTitanC4FleetBonus
#
# Used by:
# Ship: Leviathan
type = "gang"
gangBoost = "shieldCapacity"
gangBonus = "shipBonusTitanC4"
gangBonusSkill = "Caldari Titan"
runTime = "late"

def handler(fit, src, context):
    if "gang" not in context: return
    fit.ship.boostItemAttr(gangBoost, src.getModifiedItemAttr(gangBonus) * src.parent.character.getSkill(gangBonusSkill).level)


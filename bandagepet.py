vetheal = 20
emergency = int(15)
pet = 0x0002BE92
healPet = Mobiles.FindBySerial(pet)

#def GetPet():
#    petFilter = Mobiles.Filter()
#    petFilter.Enabled = True
#
#    mobs = Mobiles.ApplyFilter(petFilter)
#        
#    if len(mobs) < 1:
#        return None
#    return mobs[0]
 
#Items.UseItemByID(0x0E21, 0)
#Target.WaitForTarget(1500, False)
#Target.TargetExecute(healPet)   
#


if healPet.Hits < (healPet.HitsMax - int(5)):
    Items.UseItemByID(0x0E21, 0)
    Target.WaitForTarget(1500, False)
    Target.TargetExecute(healPet)
    if healPet.Hits < (healPet.HitsMax - emergency):
        Spells.CastMagery('Greater Heal')
        Target.WaitForTarget(1500)
        Target.TargetExecute(healPet)
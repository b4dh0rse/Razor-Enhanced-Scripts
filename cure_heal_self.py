healamount = 20

def cure():
    Spells.CastMagery("Arch Cure")
    Target.WaitForTarget(1500)
    Target.Self()
    Misc.Pause(1000)
        
def heal():
    if Player.Hits < (Player.HitsMax - healamount):
        Spells.CastMagery("Greater Heal")
        Target.WaitForTarget(1500)
        Target.Self()
        Misc.Pause(1000)
        
while Player.Poisoned:
    cure()
    
heal()
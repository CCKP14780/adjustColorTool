import maya.cmds as cmds
def adjustColorTool():
    if cmds.window('adjcol_window',q = True,ex=True):
                cmds.deleteUI('adjcol_window',window = True)
    cmds.window('adjcol_window',t='ADJUST COLOR TOOL')
    
    cmds.columnLayout(adj=True)
    cmds.optionMenuGrp('shader_opt',label='Shaders:',cc=getShaderAttrs)

############################################################################
    shds = ['----']
    shds += listExistingShaders()
    
    for shd in shds:
        cmds.menuItem(label=shd)
        
    cmds.floatSliderGrp('r_intSlider',label = 'R',field=True,min = 0,max=1)
    cmds.floatSliderGrp('g_intSlider',label = 'G',field=True,min = 0,max=1)
    cmds.floatSliderGrp('b_intSlider',label = 'B',field=True,min = 0,max=1)
    
    cmds.button('adjust_button',label='Adjust',c=adjustColor)
    
    cmds.showWindow('adjcol_window')
    cmds.window('adjcol_window',e = True,wh=[400,300])

def listExistingShaders():
    shaderTypes = cmds.listNodeTypes('shader')#list all type of shaders in maya
    
    shds = []
    
    for each in shaderTypes:
        nodes = cmds.ls(type=each)
        if nodes:
            for node in nodes:
                if not node in shds:
                    shds.append(node)                   
    return shds

def getShaderAttrs(item):
    if not item == '---':
        colR = cmds.getAttr(f'{item}.colorR')
        colG = cmds.getAttr(f'{item}.colorG')
        colB = cmds.getAttr(f'{item}.colorB')
    
        cmds.floatSliderGrp('r_intSlider',e=True,v=colR) 
        cmds.floatSliderGrp('g_intSlider',e=True,v=colG)
        cmds.floatSliderGrp('b_intSlider',e=True,v=colB)           
    else:
        cmds.floatSliderGrp('r_intSlider',e=True,v=0.0) 
        cmds.floatSliderGrp('g_intSlider',e=True,v=0.0)
        cmds.floatSliderGrp('b_intSlider',e=True,v=0.0) 

def adjustColor(*args):
    colR = cmds.floatSliderGrp('r_intSlider',q=True,v=True)
    colG = cmds.floatSliderGrp('g_intSlider',q=True,v=True)
    colB = cmds.floatSliderGrp('b_intSlider',q=True,v=True)

    shd = cmds.optionMenuGrp('shader_opt',q=True,v=True)
    
    cmds.setAttr(f'{shd}.colorR',colR)
    cmds.setAttr(f'{shd}.colorG',colG)
    cmds.setAttr(f'{shd}.colorB',colB)
     
adjustColorTool()

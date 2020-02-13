import config as c

# PT BOX


PT_BOX_ARC_1_X_1 = c.PT_BOX_X
PT_BOX_ARC_1_X_2 = c.PT_BOX_X + (c.PT_BOX_WIDTH * c.PT_BOX_ARC_PERCENTAGE * .01)
PT_BOX_ARC_2_X_1 = c.PT_BOX_X + c.PT_BOX_WIDTH
PT_BOX_ARC_2_X_2 = c.PT_BOX_X + c.PT_BOX_WIDTH + (c.PT_BOX_WIDTH * c.PT_BOX_ARC_PERCENTAGE * .01)

PT_BOX_ARC_1_Y_1 = c.PT_BOX_Y
PT_BOX_ARC_1_Y_2 = c.PT_BOX_Y + c.PT_BOX_HEIGHT
PT_BOX_ARC_2_Y_1 = c.PT_BOX_Y
PT_BOX_ARC_2_Y_2 = c.PT_BOX_Y + c.PT_BOX_HEIGHT

PT_BOX_ARC_1_START_ANGLE = 90
PT_BOX_ARC_1_END_ANGLE = 270
PT_BOX_ARC_2_START_ANGLE = 270
PT_BOX_ARC_2_END_ANGLE = 450

PT_BOX_RECT_X_1 = PT_BOX_ARC_1_X_1 + (PT_BOX_ARC_1_X_2 - PT_BOX_ARC_1_X_1) / 2
PT_BOX_RECT_X_2 = PT_BOX_ARC_2_X_1 + (PT_BOX_ARC_2_X_2 - PT_BOX_ARC_2_X_1) / 2
PT_BOX_RECT_Y_1 = c.PT_BOX_Y
PT_BOX_RECT_Y_2 = c.PT_BOX_Y + c.PT_BOX_HEIGHT

# PT BOX SHADOW

SHADOW_COLOR = c.SHADOW_COLOR

PT_BOX_SHADOW_ARC_1_X_1 = c.PT_BOX_X - c.SHADOW_WIDTH
PT_BOX_SHADOW_ARC_1_X_2 = c.PT_BOX_X + (c.PT_BOX_WIDTH * c.PT_BOX_ARC_PERCENTAGE * .01)
PT_BOX_SHADOW_ARC_2_X_1 = c.PT_BOX_X + c.PT_BOX_WIDTH
PT_BOX_SHADOW_ARC_2_X_2 = c.PT_BOX_X + c.PT_BOX_WIDTH + (
        c.PT_BOX_WIDTH * c.PT_BOX_ARC_PERCENTAGE * .01) + c.SHADOW_WIDTH

PT_BOX_SHADOW_ARC_1_Y_1 = c.PT_BOX_Y - c.SHADOW_WIDTH
PT_BOX_SHADOW_ARC_1_Y_2 = c.PT_BOX_Y + c.PT_BOX_HEIGHT + c.SHADOW_WIDTH
PT_BOX_SHADOW_ARC_2_Y_1 = c.PT_BOX_Y - c.SHADOW_WIDTH
PT_BOX_SHADOW_ARC_2_Y_2 = c.PT_BOX_Y + c.PT_BOX_HEIGHT + c.SHADOW_WIDTH

PT_BOX_SHADOW_ARC_1_START_ANGLE = 90
PT_BOX_SHADOW_ARC_1_END_ANGLE = 270
PT_BOX_SHADOW_ARC_2_START_ANGLE = 270
PT_BOX_SHADOW_ARC_2_END_ANGLE = 450

PT_BOX_SHADOW_RECT_X_1 = PT_BOX_SHADOW_ARC_1_X_1 + (PT_BOX_SHADOW_ARC_1_X_2 - PT_BOX_SHADOW_ARC_1_X_1) / 2
PT_BOX_SHADOW_RECT_X_2 = PT_BOX_SHADOW_ARC_2_X_1 + (PT_BOX_SHADOW_ARC_2_X_2 - PT_BOX_SHADOW_ARC_2_X_1) / 2
PT_BOX_SHADOW_RECT_Y_1 = c.PT_BOX_Y - c.SHADOW_WIDTH
PT_BOX_SHADOW_RECT_Y_2 = c.PT_BOX_Y + c.PT_BOX_HEIGHT + c.SHADOW_WIDTH

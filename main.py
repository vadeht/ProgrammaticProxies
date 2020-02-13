from PIL import Image, ImageFont, ImageDraw
import co


def draw_pt_box(draw, color):
    # PT BOX Shadow?
    draw.chord(
        (
            co.PT_BOX_SHADOW_ARC_1_X_1, co.PT_BOX_SHADOW_ARC_1_Y_1, co.PT_BOX_SHADOW_ARC_1_X_2,
            co.PT_BOX_SHADOW_ARC_1_Y_2),
        co.PT_BOX_SHADOW_ARC_1_START_ANGLE,
        co.PT_BOX_SHADOW_ARC_1_END_ANGLE,
        fill=co.SHADOW_COLOR
    )
    draw.chord(
        (
            co.PT_BOX_SHADOW_ARC_2_X_1, co.PT_BOX_SHADOW_ARC_2_Y_1, co.PT_BOX_SHADOW_ARC_2_X_2,
            co.PT_BOX_SHADOW_ARC_2_Y_2),
        co.PT_BOX_SHADOW_ARC_2_START_ANGLE,
        co.PT_BOX_SHADOW_ARC_2_END_ANGLE,
        fill=co.SHADOW_COLOR
    )
    draw.rectangle(
        (co.PT_BOX_SHADOW_RECT_X_1, co.PT_BOX_SHADOW_RECT_Y_1, co.PT_BOX_SHADOW_RECT_X_2, co.PT_BOX_SHADOW_RECT_Y_2),
        fill=co.SHADOW_COLOR
    )

    # PT BOX?
    draw.chord(
        (co.PT_BOX_ARC_1_X_1, co.PT_BOX_ARC_1_Y_1, co.PT_BOX_ARC_1_X_2, co.PT_BOX_ARC_1_Y_2),
        co.PT_BOX_ARC_1_START_ANGLE,
        co.PT_BOX_ARC_1_END_ANGLE,
        fill=color
    )
    draw.chord(
        (co.PT_BOX_ARC_2_X_1, co.PT_BOX_ARC_2_Y_1, co.PT_BOX_ARC_2_X_2, co.PT_BOX_ARC_2_Y_2),
        co.PT_BOX_ARC_2_START_ANGLE,
        co.PT_BOX_ARC_2_END_ANGLE,
        fill=color
    )
    draw.rectangle(
        (co.PT_BOX_RECT_X_1, co.PT_BOX_RECT_Y_1, co.PT_BOX_RECT_X_2, co.PT_BOX_RECT_Y_2),
        fill=color
    )


def main():
    canvas = Image.new('RGBA', (5000, 5000), (130, 20, 200, 255))
    draw = ImageDraw.Draw(canvas, 'RGBA')

    draw_pt_box(draw, (100, 0, 30))

    '''
    # Title Shadow?
    draw.chord((150, 150, 400, 650), 90, 270, fill=(100, 100, 50), width=0)
    draw.chord((2800, 150, 3050, 650), 270, 450, fill=(100, 100, 50), width=0)
    draw.rectangle((250, 150, 2950, 650), fill=(100, 100, 50), width=0)

    # Title BOX?
    draw.chord((200, 200, 400, 600), 90, 270, fill=(200, 100, 50), width=0)
    draw.chord((2800, 200, 3000, 600), 270, 450, fill=(200, 100, 50), width=0)
    draw.rectangle((300, 200, 2900, 600), fill=(200, 100, 50), width=0)
    '''

    canvas.save('./out/canvas.png')


if __name__ == '__main__':
    main()

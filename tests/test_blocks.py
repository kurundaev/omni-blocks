from django.test import TestCase
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.blocks.field_block import RawHTMLBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.tests.utils import Image, get_test_image_file

from omni_blocks import blocks as internal_blocks


class TestBodyStreamBlock(TestCase):
    """Tests for the BodyStreamBlock."""
    def setUp(self):
        self.block = internal_blocks.BodyStreamBlock
        self.children = self.block().child_blocks

    def test_parent_class(self):
        """Test BodyStreamBlock is a subclass of StreamBlock."""
        self.assertTrue(issubclass(self.block, blocks.StreamBlock))

    def test_attributes(self):
        """Test BodyStreamBlock's attributes are correct."""
        expected = [
            'basic_card_grid',
            'block_quote',
            'button',
            'google_map',
            'h1',
            'h2',
            'h3',
            'h4',
            'image',
            'image_grid',
            'linked_image_grid',
            'ordered_list',
            'paragraph',
            'pull_quote',
            'raw_html',
            'related_page',
            'table',
            'two_column',
            'unordered_list',
        ]
        self.assertEqual(list(self.children.keys()), expected)

    def test_basic_card_grid(self):
        """Test BodyStreamBlock.basic_card_grid has the expected parent."""
        block = self.children.get('basic_card_grid')

        self.assertIsInstance(block, internal_blocks.BasicCardGridBlock)

    def test_block_quote(self):
        """Test BodyStreamBlock.block_quote has the expected parent."""
        block = self.children.get('block_quote')

        self.assertIsInstance(block, blocks.BlockQuoteBlock)

    def test_button_block(self):
        """Test BodyStreamBlock.button_block has the expected parent."""
        block = self.children.get('button')

        self.assertIsInstance(block, internal_blocks.ButtonBlock)

    def test_google_map(self):
        """Test BodyStreamBlock.google_map has the expected parent."""
        block = self.children.get('google_map')

        self.assertIsInstance(block, internal_blocks.GoogleMapBlock)

    def test_h1(self):
        """Test BodyStreamBlock.h1 has the expected parent."""
        block = self.children.get('h1')

        self.assertIsInstance(block, internal_blocks.HBlock)

    def test_h2(self):
        """Test BodyStreamBlock.h2 has the expected parent."""
        block = self.children.get('h2')

        self.assertIsInstance(block, internal_blocks.HBlock)

    def test_h3(self):
        """Test BodyStreamBlock.h3 has the expected parent."""
        block = self.children.get('h3')

        self.assertIsInstance(block, internal_blocks.HBlock)

    def test_h4(self):
        """Test BodyStreamBlock.h4 has the expected parent."""
        block = self.children.get('h4')

        self.assertIsInstance(block, internal_blocks.HBlock)

    def test_image(self):
        """Test BodyStreamBlock.image has the expected parent."""
        block = self.children.get('image')

        self.assertIsInstance(block, ImageChooserBlock)

    def test_image_grid(self):
        """Test BodyStreamBlock.image_grid has the expected parent."""
        block = self.children.get('image_grid')

        self.assertIsInstance(block, internal_blocks.ImageGridBlock)

    def test_linked_image_grid(self):
        """Test BodyStreamBlock.linked_image_grid has the expected parent."""
        block = self.children.get('linked_image_grid')

        self.assertIsInstance(block, internal_blocks.LinkedImageGridBlock)

    def test_ordered_list(self):
        """Test BodyStreamBlock.ordered_list has the expected parent."""
        block = self.children.get('ordered_list')

        self.assertIsInstance(block, internal_blocks.OLBlock)

    def test_paragraph(self):
        """Test BodyStreamBlock.paragraph has the expected parent."""
        block = self.children.get('paragraph')

        self.assertIsInstance(block, blocks.RichTextBlock)

    def test_pull_quote(self):
        """Test BodyStreamBlock.pull_quote has the expected parent."""
        block = self.children.get('pull_quote')

        self.assertIsInstance(block, internal_blocks.PullQuoteBlock)

    def test_raw_html(self):
        """Test BodyStreamBlock.raw_html has the expected parent."""
        block = self.children.get('raw_html')

        self.assertIsInstance(block, RawHTMLBlock)

    def test_related_page(self):
        """Test BodyStreamBlock.related_page has the expected parent."""
        block = self.children.get('related_page')

        self.assertIsInstance(block, internal_blocks.PageChooserTemplateBlock)

    def test_table(self):
        """Test BodyStreamBlock.table has the expected parent."""
        block = self.children.get('table')

        self.assertIsInstance(block, TableBlock)

    def test_two_column(self):
        """Test BodyStreamBlock.two_column has the expected parent."""
        block = self.children.get('two_column')

        self.assertIsInstance(block, internal_blocks.TwoColumnBlock)

    def test_unordered_list(self):
        """Test BodyStreamBlock.unordered_list has the expected parent."""
        block = self.children.get('unordered_list')

        self.assertIsInstance(block, internal_blocks.ULBlock)


class TestHBlock(TestCase):
    """Tests for the HBlock."""
    def test_parent_class(self):
        """Test HBlock is a subclass of CharBlock."""
        self.assertTrue(issubclass(internal_blocks.HBlock, blocks.CharBlock))

    def test_render(self):
        """Test HBlock.render renders as expected."""
        block = internal_blocks.HBlock('h2')
        expected = '<h2>some text</h2>'
        result = block.render('some text', context={})

        self.assertEqual(result, expected)


class TestPullQuoteBlock(TestCase):
    """Tests for the PullQuoteBlock."""
    def test_parent_class(self):
        """Test PullQuoteBlock is a subclass of CharBlock."""
        self.assertTrue(issubclass(internal_blocks.PullQuoteBlock, blocks.CharBlock))

    def test_render(self):
        """Test PullQuoteBlock.render renders as expected."""
        block = internal_blocks.PullQuoteBlock()
        expected = '<blockquote class="pquote">some text</blockquote>'
        result = block.render('some text', context={})

        self.assertEqual(result, expected)


class TestLinkBlock(TestCase):

    def setUp(self):
        self.page = Page.objects.create(
            title='Omni',
            slug='omni-digital',
            depth=4,
            path='000100010001'
        )

    def test_external_url_renders(self):
        """Ensure the block renders in isolation."""
        link_block = internal_blocks.LinkBlock()
        value = link_block.to_python({
            'external_url': 'https://omni-digital.co.uk',
            'internal_url': self.page.pk,
        })
        content = link_block.render(value)
        self.assertEqual('https://omni-digital.co.uk', content)

    def test_external_url_renders_when_nested(self):
        """Ensure the block renders as expected when it's nested within another block"""
        bc_block = internal_blocks.BasicCardBlock()
        value = bc_block.to_python(
            {
                'title': 'cool',
                'link': {
                    'external_url': 'https://omni-digital.co.uk',
                    'internal_url': self.page.pk,
                }
            }
        )
        card_content = bc_block.render(value)
        self.assertIn('<a href="https://omni-digital.co.uk">cool</a>', card_content)

    def test_internal_url_renders(self):
        """Ensure that the internal_url renders as expected."""
        link_block = internal_blocks.LinkBlock()
        value = link_block.render({
            'internal_url': self.page,
        })
        self.assertEqual(value, '/omni-digital/')

    def test_internal_url_renders_when_nested(self):
        """Ensure the block renders as expected when it's nested within another block"""
        bc_block = internal_blocks.BasicCardBlock()
        value = bc_block.to_python(
            {
                'title': 'cool',
                'link': {
                    'internal_url': self.page.pk,
                }
            }
        )
        card_content = bc_block.render(value)
        self.assertIn('<a href="/omni-digital/">cool</a>', card_content)


class TestLinkedImageBlock(TestCase):

    def setUp(self):
        self.image = Image.objects.create(
            title="Test image",
            file=get_test_image_file(),
        )

    def test_image_link(self):
        """Ensure that the image link renders correctly"""
        linked_image_block = internal_blocks.LinkedImageBlock()
        value = linked_image_block.to_python({
            'image': self.image.pk,
            'link': {
                'external_url': 'https://omni-digital.co.uk',
            },
        })
        self.assertIn(
            '<a href="https://omni-digital.co.uk"><img alt="Test image"', linked_image_block.render(value))


class TestTitledLinkBlock(TestCase):

    def test_renders(self):
        """Ensure that the block renders as expected."""
        titled_link_block = internal_blocks.TitledLinkBlock()
        value = titled_link_block.to_python({
            'title': 'Omni Digital',
            'link': {
                'external_url': 'https://omni-digital.co.uk',
            },
        })
        self.assertIn(
            '<a href="https://omni-digital.co.uk">Omni Digital</a>', titled_link_block.render(value))


class TestButtonBlock(TestCase):

    def test_renders(self):
        """Ensure that the block renders as expected."""
        button_block = internal_blocks.ButtonBlock()
        value = button_block.to_python({
            'title': 'Omni Digital',
            'link': {
                'external_url': 'https://omni-digital.co.uk',
            },
        })
        self.assertIn(
            '<p class="button">', button_block.render(value))
        self.assertIn(
            '<a href="https://omni-digital.co.uk">Omni Digital</a>', button_block.render(value))

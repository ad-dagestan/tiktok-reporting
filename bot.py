class TikTokReportingBot:
    """
    A bot that detects and reports inappropriate content on TikTok.
    """

    def __init__(self):
        # Initialize the bot
        pass

    def detect_content(self, content):
        """
        Analyze the content for inappropriate material.
        :param content: The content to be analyzed.
        :return: True if inappropriate, False otherwise.
        """
        # Placeholder implementation
        return "inappropriate" in content.lower()

    def report_content(self, content):
        """
        Report the inappropriate content.
        :param content: The content to be reported.
        """
        # Placeholder implementation
        print(f'Reporting content: {content}')

    def process_content(self, content):
        """
        Process the content for detection and reporting.
        :param content: The content to be processed.
        """
        if self.detect_content(content):
            self.report_content(content)
        else:
            print("Content is appropriate.")

#  noqa: INP001
#  SPDX-FileCopyrightText: 2024-present Hinrich Mahler <chango@mahlerhome.de>
#
#  SPDX-License-Identifier: MIT

from chango.concrete import (
    DirectoryChanGo,
    DirectoryVersionScanner,
    HeaderVersionHistory,
)
from chango.concrete.sections import GitHubSectionChangeNote, Section, SectionVersionNote

CustomChangeNote = GitHubSectionChangeNote.with_sections(
    [
        Section(uid="req_section", title="Required Section", is_required=True),
        Section(uid="opt_section", title="Optional Sectionnnnn"),
    ]
)

chango_instance = DirectoryChanGo(
    change_note_type=CustomChangeNote,
    version_note_type=SectionVersionNote,
    version_history_type=HeaderVersionHistory,
    scanner=DirectoryVersionScanner(base_directory=".", unreleased_directory="unreleased"),
)
